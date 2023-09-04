""":mod:`kamis.models.common` --- KAMIS 오픈 API 공통 모델 모듈
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

KAMIS 오픈 API의 요청에 필요한 공통된 모델들을 정의한 모듈입니다.

"""
from dataclasses import dataclass
import enum
from typing import Dict, List, Union


__all__ = 'Country', 'Direction', 'BasicResponse', 'ProductClass', 'ResultCode'


class Country(enum.Enum):
    """지역"""
    SEOUL = '1101'
    BUSAN = '2100'
    DAEGU = '2200'
    INCHEON = '2300'
    GWANGJU = '2401'
    DAEJEON = '2501'
    ULSAN = '2601'
    SUWON = '3111'
    CHUNCHEON = '3211'
    CHEONGJU = '3311'
    JEONJU = '3511'
    POHANG = '3711'
    JEJU = '3911'
    UIJEONGBU = '3113'
    SUNCHEON = '3613'
    ANDONG = '3714'
    CHANGWON = '3814'
    YONGIN = '3145'


class Direction(enum.Enum):
    """등락여부"""
    #: 가격하락
    DECREASE = '0'
    #: 가격상승
    INCREASE = '1'
    #: 등락없음
    NO_CHANGE = '2'


class ProductClass(enum.Enum):
    """품목구분"""
    #: 소매
    RETAIL = '01'
    #: 도매
    WHOLESALE = '02'


class ResultCode(enum.Enum):
    """비고/에러 메세지"""
    #: 성공
    SUCCESS = '000'
    #: 결과 없음
    NO_DATA = '001'
    #: 잘못된 파라미터
    WRONG_PARAMETERS = '200'
    #: 인증되지 않은 요청
    UNAUTHENTICATED_REQUEST = '900'

    @property
    def succeeded(self):
        return self in (ResultCode.SUCCESS, ResultCode.NO_DATA)


@dataclass(frozen=True)
class BasicResponse:
    """모든 요청의 응답에 공통적으로 포함되어 있는 값을 갖는 클래스입니다."""
    #: API 문서의 "요청 메세지"
    condition: Union[List[List[str]], Dict[str, str]]
