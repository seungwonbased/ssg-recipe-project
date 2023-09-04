""":mod:`kamis.client` --- KAMIS 오픈 API 클라이언트 모듈
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

KAMIS 오픈 API를 실행하기 위한 클래스 :class:`KamisOpenApi`를 정의한
모듈입니다.

"""
from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Union
import urllib.parse

from requests import get

from .models.common import ResultCode
from .models.daily_sales_list import (
    PriceResponse as DailySalesListPriceResponse,
    Response as DailySalesListResponse,
)
from .models.period_product_list import (
    DataResponse as PeriodProductListDataResponse,
    ItemResponse as PeriodProductListItemResponse,
    Parameters as PeriodProductListParameters,
    Response as PeriodProductListResponse,
)


__all__ = 'CertificationPair', 'KamisOpenApi'


@dataclass
class CertificationPair:
    """인증 정보를 담는 클래스입니다."""
    #: 인증 키
    cert_key: str
    #: 요청자 아이디
    cert_id: str


class KamisOpenApi:
    """오픈 API를 실행할 수 있는 클라이언트 클래스입니다."""

    def __init__(
        self,
        cert: CertificationPair,
        endpoint: str = "http://www.kamis.or.kr/service/price/xml.do"
    ):
        self.cert = cert
        self.endpoint = endpoint

    def build_action_endpoint(
        self,
        action: str,
        parameters: Dict[str, Union[str, List[str]]] = {}
    ) -> str:
        completed_parameters = parameters.copy()
        completed_parameters.update({
            'action': action,
            'p_cert_id': self.cert.cert_id,
            'p_cert_key': self.cert.cert_key,
            'p_returntype': 'json',
        })
        parsed_url = urllib.parse.urlparse(self.endpoint)._replace(
            query=urllib.parse.urlencode(completed_parameters, doseq=True)
        )
        return urllib.parse.urlunparse(parsed_url)

    def request(self, action_endpoint: str) -> Dict[str, Any]:
        response = get(action_endpoint)
        response.raise_for_status()
        return response.json()

    def daily_sales_list(self) -> DailySalesListResponse:
        endpoint = self.build_action_endpoint('dailySalesList')
        response = self.request(endpoint)
        if response['error_code'] == ResultCode.SUCCESS.value:
            parsed_price = []
            for price in response['price']:
                parsed_price.append(DailySalesListPriceResponse(**price))
            response['price'] = parsed_price
        return DailySalesListResponse(**response)

    def period_product_list(
        self, params: PeriodProductListParameters
    ) -> PeriodProductListResponse:
        endpoint = self.build_action_endpoint(
            'periodProductList',
            {k: v for k, v in asdict(params).items() if v is not None}
        )
        response = self.request(endpoint)
        data = response.get('data')
        if data and isinstance(data, dict):
            parsed_item = []
            for item in data['item']:
                parsed_item.append(PeriodProductListItemResponse(**item))
            data['item'] = parsed_item
            response['data'] = PeriodProductListDataResponse(**data)
        return PeriodProductListResponse(**response)
