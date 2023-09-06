""":mod:`kamis.models.period_product_list` --- PeriodProductList API 모델
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

KAMIS 오픈 API 중 PeriodProductList API의 파라미터 및 응답에 대응하는 모델을
정의한 모듈입니다.

https://www.kamis.or.kr/customer/reference/openapi_list.do?action=detail&boardno=2

"""
from dataclasses import InitVar, dataclass, field
import datetime
from typing import List, Optional, Tuple, Union

from .common import BasicResponse, Country, ProductClass, ResultCode


__all__ = 'DataResponse', 'ItemResponse', 'Parameters', 'Response'


@dataclass
class Parameters:
    """PeriodProductList API 요청에 필요한 파라미터를 담는 클래스입니다."""
    #: 조회 기간
    date_range: InitVar[Tuple[datetime.date, datetime.date]]
    #: API 문서의 요청 변수 중 "조회기간(start date)"
    #: `date_range` 값을 통해 만들어집니다.
    p_startday: str = field(init=False)
    #: API 문서의 요청 변수 중 "조회기간(end date)"
    #: `date_range` 값을 통해 만들어집니다.
    p_endday: str = field(init=False)
    #: 품목 구분
    product_class: InitVar[Optional[ProductClass]]
    #: API 문서의 요청 변수 중 "구분 ( 01:소매, 02:도매, default:02 )"
    #: `product_class` 값을 통해 만들어집니다.
    p_productclscode: Optional[str] = field(init=False, default=None)
    #: 부류 코드
    item_category_code: InitVar[str]
    #: API 문서의 요청 변수 중 "부류코드"
    #: `item_category_code` 값을 통해 만들어집니다.
    p_itemcategorycode: str = field(init=False)
    #: 품목 코드
    item_code: InitVar[str]
    #: API 문서의 요청 변수 중 "품목코드"; `item_code` 값을 통해 만들어집니다.
    p_itemcode: str = field(init=False)
    #: 품종 코드
    kind_code: InitVar[str]
    #: API 문서의 요청 변수 중 "품종코드"; `kind_code` 값을 통해 만들어집니다.
    p_kindcode: str = field(init=False)
    #: 등급 코드
    product_rank_code: InitVar[str]
    #: API 문서의 요청 변수 중 "등급코드"
    #: `product_rank_code` 값을 통해 만들어집니다.
    p_productrankcode: str = field(init=False)
    #: 지역
    county: InitVar[Optional[Country]]
    #: API 문서의 요청 변수 중 "지역"; `county` 값을 통해 만들어집니다.
    #: 이하 문서상 설명:
    #:  소매가격 선택가능 지역 (
    #:    1101:서울, 2100:부산, 2200:대구, 2300:인천, 2401:광주,
    #:    2501:대전, 2601:울산, 3111:수원, 3211:춘천, 3311:청주, 3511:전주,
    #:    3711:포항, 3911:제주, 3113:의정부, 3613:순천, 3714:안동, 3814:창원,
    #:    3145:용인
    #:  )
    #:  도매가격 선택가능 지역 (
    #:    1101:서울, 2100:부산, 2200:대구, 2401:광주, 2501:대전
    #:  )
    #:  default : 전체지역
    p_countycode: Optional[str] = field(init=False, default=None)
    #: kg 단위 환산 여부
    convert_kg: InitVar[Optional[bool]]
    #: API 문서의 요청 변수 중 "kg단위 환산여부"
    #: `convert_kg` 값을 통해 만들어집니다.
    #: 이하 문서상 설명:
    #:   Y : 1kg 단위표시, N : 정보조사 단위표시, ex: 쌀 20kg
    #:   default : N
    p_convert_kg_yn: Optional[str] = field(init=False, default=None)

    def __post_init__(
        self, date_range: Tuple[datetime.date, datetime.date],
        product_class: Optional[ProductClass], item_category_code: str,
        item_code: str, kind_code: str, product_rank_code: str,
        county: Optional[Country], convert_kg: Optional[bool]
    ):
        self.p_startday = date_range[0].isoformat()
        self.p_endday = date_range[1].isoformat()
        if product_class:
            self.p_productclscode = product_class.value
        self.p_itemcategorycode = item_category_code
        self.p_itemcode = item_code
        self.p_kindcode = kind_code
        self.p_productrankcode = product_rank_code
        if county:
            self.p_countycode = county.value
        if convert_kg:
            self.p_convert_kg_yn = 'Y' if convert_kg else 'N'


@dataclass(frozen=True)
class ItemResponse:
    #: API 문서의 "품목명"
    itemname: InitVar[Union[str, List]]
    #: "품목명"; `itemname` 값을 통해 만들어집니다.
    item_name: Optional[str] = field(init=False)
    #: API 문서의 "품종명"
    kindname: InitVar[Union[str, List]]
    #: "품종명"; `kindname` 값을 통해 만들어집니다.
    kind_name: Optional[str] = field(init=False)
    #: API 문서의 "시군구"
    countyname: InitVar[str]
    #: "시군구"; `countyname` 값을 통해 만들어집니다.
    county_name: str = field(init=False)
    #: API 문서의 "마켓명"
    marketname: InitVar[Union[str, List]]
    #: "마켓명"; `marketname` 값을 통해 만들어집니다.
    market_name: Optional[str] = field(init=False)
    #: API 문서의 "연도"
    yyyy: InitVar[str]
    #: API 문서의 "날짜"
    regday: InitVar[str]
    #: 조사일; `yyyy` 및 `regday` 값을 통해 만들어집니다.
    reg_date: datetime.date = field(init=False)
    #: API 문서의 "가격"
    price: InitVar[str]
    #: "가격"; `price` 값을 통해 만들어집니다.
    price_: Optional[int] = field(init=False)

    def __post_init__(
        self, itemname: Union[str, List], kindname: Union[str, List],
        countyname: str, marketname: Union[str, List], yyyy: str, regday: str,
        price: str
    ):
        object.__setattr__(self, 'item_name', itemname if itemname else None)
        object.__setattr__(self, 'kind_name', kindname if kindname else None)
        object.__setattr__(self, 'county_name', countyname)
        object.__setattr__(
            self, 'market_name', marketname if marketname else None
        )
        object.__setattr__(
            self,
            'reg_date',
            datetime.date.fromisoformat(f'{yyyy}-{regday.replace("/", "-")}')
        )
        object.__setattr__(
            self,
            'price_',
            int(price.replace(',', '')) if price != '-' else None
        )


@dataclass(frozen=True)
class DataResponse:
    #: 품목 가격 정보
    item: InitVar[List[ItemResponse]]
    #: 품목 가격 정보; `item` 값을 통해 만들어집니다.
    items: List[ItemResponse] = field(init=False)
    #: API 문서의 "결과코드"; 문서상으로는 result_code로 표기되어 있습니다.
    error_code: InitVar[str]
    #: 결과 코드; `error_code` 값을 통해 만들어집니다.
    result_code: ResultCode = field(init=False)

    def __post_init__(self, item: List[ItemResponse], error_code: str):
        object.__setattr__(self, 'items', item)
        object.__setattr__(self, 'result_code', ResultCode(error_code))


@dataclass(frozen=True)
class Response(BasicResponse):
    #: API 결과 응답 본문
    data: InitVar[Union[DataResponse, List[str]]]
    #: API 결과; `data` 값을 통해 만들어집니다.
    data_: DataResponse = field(init=False)

    def __post_init__(self, data: Union[DataResponse, List[str]]):
        object.__setattr__(
            self,
            'data_',
            data if isinstance(data, DataResponse) else DataResponse(
                item=[], error_code=data[0]
            )
        )
