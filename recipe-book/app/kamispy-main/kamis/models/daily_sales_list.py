""":mod:`kamis.models.daily_sales_list` --- DailySalesList API 모델
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

KAMIS 오픈 API 중 DailySalesList API의 응답에 대응하는 모델을 정의한
모듈입니다.

https://www.kamis.or.kr/customer/reference/openapi_list.do?action=detail&boardno=6

"""
import collections
from dataclasses import InitVar, dataclass, field
import datetime
from typing import List, Optional, OrderedDict as OrderedDictType, Union

from .common import BasicResponse, Direction, ProductClass, ResultCode


__all__ = 'PriceResponse', 'Response'


@dataclass(frozen=True)
class PriceResponse:
    #: API 문서의 "구분(01:소매, 02:도매)"
    product_cls_code: InitVar[str]
    #: API 문서의 "구분 이름"; 사용되지 않습니다.
    product_cls_name: InitVar[str]
    #: 품목 구분; `product_cls_code` 값을 통해 만들어집니다.
    product_class: ProductClass = field(init=False)
    #: API 문서의 "부류코드"
    category_code: str
    #: API 문서의 "부류명"
    category_name: str
    #: API 문서의 "품목코드"
    productno: str
    #: API 문서의 "최근조사일"
    lastest_day: InitVar[str]
    #: 최근 조사일; `lastest_day` 값을 통해 만들어집니다.
    latest_date: datetime.date = field(init=False)
    #: API 문서의 "품목명"
    productName: InitVar[str]
    #: 품목명; `productName` 값을 통해 만들어집니다.
    product_name: str = field(init=False)
    #: API 문서의 "품목명"
    item_name: str
    #: API 문서의 "단위"
    unit: str
    #: API 문서의 "최근 조사일자"
    day1: InitVar[str]
    #: API 문서의 "최근 조사일자 가격"
    dpr1: InitVar[Union[List, str]]
    #: API 문서의 "1일전 일자"
    day2: InitVar[str]
    #: API 문서의 "1일전 가격"
    dpr2: InitVar[Union[List, str]]
    #: API 문서의 "1개월전 일자"
    day3: InitVar[str]
    #: API 문서의 "1개월전 가격"
    dpr3: InitVar[Union[List, str]]
    #: API 문서의 "1년전 일자"
    day4: InitVar[str]
    #: API 문서의 "1년전 가격"
    dpr4: InitVar[Union[List, str]]
    #: 일자별 가격; `day[1-4]` 및 `dpr[1-4]` 값을 통해 만들어집니다.
    date_price_dict: OrderedDictType[str, Optional[int]] = field(init=False)
    #: API 문서의 "등락여부( 0:가격하락 1:가격상승 2:등락없음 )"
    direction: InitVar[str]
    #: 등락여부; `direction` 값을 통해 만들어집니다.
    direction_type: Direction = field(init=False)
    #: API 문서의 "등락율"
    value: InitVar[str]
    #: 등락율; `value` 값을 통해 만들어집니다.
    direction_value: float = field(init=False)

    def __post_init__(
        self, product_cls_code: str, product_cls_name: str, lastest_day: str,
        productName: str, day1: str, dpr1: Union[List, str], day2: str,
        dpr2: Union[List, str], day3: str, dpr3: Union[List, str], day4: str,
        dpr4: Union[List, str], direction: str, value: str
    ):
        object.__setattr__(
            self, 'product_class', ProductClass(product_cls_code)
        )
        object.__setattr__(
            self, 'latest_date', datetime.date.fromisoformat(lastest_day)
        )
        object.__setattr__(self, 'product_name', productName)
        date_price_dict = collections.OrderedDict()
        date_price_dict[day1] = int(dpr1.replace(',', '')) if dpr1 else None
        date_price_dict[day2] = int(dpr2.replace(',', '')) if dpr2 else None
        date_price_dict[day3] = int(dpr3.replace(',', '')) if dpr3 else None
        date_price_dict[day4] = int(dpr4.replace(',', '')) if dpr4 else None
        object.__setattr__(self, 'date_price_dict', date_price_dict)
        object.__setattr__(self, 'direction_type', Direction(direction))
        object.__setattr__(self, 'direction_value', float(value))


@dataclass(frozen=True)
class Response(BasicResponse):
    #: API 문서의 "응답 메세지"
    price: InitVar[Union[List[PriceResponse], str]]
    #: 응답 메세지; `price` 값을 통해 만들어집니다.
    prices: Optional[List[PriceResponse]] = field(init=False)
    #: API 문서의 "결과코드"; 문서상으로는 result_code로 표기되어 있습니다.
    error_code: InitVar[str]
    #: 결과 코드; `error_code` 값을 통해 만들어집니다.
    result_code: ResultCode = field(init=False)

    def __post_init__(self, price: PriceResponse, error_code: str):
        object.__setattr__(
            self, 'prices', price if isinstance(price, list) else None
        )
        object.__setattr__(self, 'result_code', ResultCode(error_code))
