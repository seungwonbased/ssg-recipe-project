import datetime
import urllib.parse

from pytest import fixture, raises
from requests.exceptions import HTTPError
from requests_mock import Mocker

from kamis.client import CertificationPair, KamisOpenApi
from kamis.models.common import Direction, ResultCode
from kamis.models.daily_sales_list import (
    PriceResponse as DailySalesListPriceResponse,
    Response as DailySalesListResponse,
)
from kamis.models.period_product_list import (
    DataResponse as PeriodProductListDataResponse,
    ItemResponse as PeriodProductListItemResponse,
    Parameters as PeriodProductListParameters,
    Response as PeriodProductListResponse,
)


@fixture
def fx_kamis_open_api():
    return KamisOpenApi(
        CertificationPair('testKey', 'testId'),
        'http://kamis.example.com/example.do'
    )


@fixture
def fx_period_product_list_parameters():
    return PeriodProductListParameters(
        date_range=(datetime.date(2020, 10, 21), datetime.date(2020, 10, 22)),
        product_class=None, item_category_code='100', item_code='111',
        kind_code='01', product_rank_code='04', county=None, convert_kg=None
    )


def assert_url_same(a: str, b: str):
    a = urllib.parse.urlparse(a)
    b = urllib.parse.urlparse(b)
    assert a.scheme == b.scheme
    assert a.netloc == b.netloc
    assert a.path == b.path
    assert a.params == b.params
    assert urllib.parse.parse_qs(a.query) == urllib.parse.parse_qs(b.query)
    assert a.fragment == b.fragment


def test_kamis_open_api_build_action_endpoint(fx_kamis_open_api: KamisOpenApi):
    assert_url_same(
        fx_kamis_open_api.build_action_endpoint(
            'helloApi',
            {
                'this': 'is',
                'custom': 'parameter',
                'include': ['listed', 'parameter'],
            }
        ),
        'http://kamis.example.com/example.do?action=helloApi'
        '&p_cert_id=testId&p_cert_key=testKey&p_returntype=json'
        '&this=is&custom=parameter&include=listed&include=parameter'
    )


def test_kamis_open_api_request(fx_kamis_open_api: KamisOpenApi):
    with Mocker() as m:
        m.get('http://kamis.example.com/example.do', json={})
        fx_kamis_open_api.request('http://kamis.example.com/example.do')
        assert len(m.request_history) == 1


def test_kamis_open_api_request_raise_exc(fx_kamis_open_api: KamisOpenApi):
    with Mocker() as m:
        m.get('http://kamis.example.com/example.do', json={}, status_code=500)
        with raises(HTTPError):
            fx_kamis_open_api.request('http://kamis.example.com/example.do')
        assert len(m.request_history) == 1


def test_kamis_open_api_daily_sales_list(fx_kamis_open_api: KamisOpenApi):
    with Mocker() as m:
        m.get(
            'http://kamis.example.com/example.do',
            json={
                'condition': [['20201016']],
                'error_code': '000',
                'price': [
                    {
                        'category_code': '100',
                        'category_name': '식량작물',
                        'day1': '당일',
                        'day2': '1일전',
                        'day3': '1개월전',
                        'day4': '1년전',
                        'direction': '1',
                        'dpr1': '55,094',
                        'dpr2': '55,053',
                        'dpr3': '52,723',
                        'dpr4': '51,034',
                        'item_name': '쌀/일반계',
                        'lastest_day': '2020-10-16',
                        'productName': '쌀/일반계',
                        'product_cls_code': '01',
                        'product_cls_name': '소매',
                        'productno': '272',
                        'unit': '20kg',
                        'value': '0.1',
                    },
                    {
                        'category_code': '100',
                        'category_name': '식량작물',
                        'day1': '당일',
                        'day2': '1일전',
                        'day3': '1개월전',
                        'day4': '1년전',
                        'direction': '0',
                        'dpr1': '58,887',
                        'dpr2': '58,939',
                        'dpr3': [],
                        'dpr4': '53,015',
                        'item_name': '쌀/햇일반계',
                        'lastest_day': '2020-10-16',
                        'productName': '쌀/햇일반계',
                        'product_cls_code': '01',
                        'product_cls_name': '소매',
                        'productno': '273',
                        'unit': '20kg',
                        'value': '0.1',
                    },
                ],
            }
        )
        daily_sales_list = fx_kamis_open_api.daily_sales_list()
        assert daily_sales_list == DailySalesListResponse(
            condition=[['20201016']],
            error_code=ResultCode.SUCCESS.value,
            price=[
                DailySalesListPriceResponse(
                    product_cls_code='01',
                    product_cls_name='소매',
                    category_code='100',
                    category_name='식량작물',
                    productno='272',
                    lastest_day='2020-10-16',
                    productName='쌀/일반계',
                    item_name='쌀/일반계',
                    unit='20kg',
                    day1='당일',
                    dpr1='55,094',
                    day2='1일전',
                    dpr2='55,053',
                    day3='1개월전',
                    dpr3='52,723',
                    day4='1년전',
                    dpr4='51,034',
                    direction=Direction.INCREASE.value,
                    value='0.1'
                ),
                DailySalesListPriceResponse(
                    product_cls_code='01',
                    product_cls_name='소매',
                    category_code='100',
                    category_name='식량작물',
                    productno='273',
                    lastest_day='2020-10-16',
                    productName='쌀/햇일반계',
                    item_name='쌀/햇일반계',
                    unit='20kg',
                    day1='당일',
                    dpr1='58,887',
                    day2='1일전',
                    dpr2='58,939',
                    day3='1개월전',
                    dpr3=[],
                    day4='1년전',
                    dpr4='53,015',
                    direction=Direction.DECREASE.value,
                    value='0.1'
                ),
            ]
        )
        assert len(m.request_history) == 1


def test_kamis_open_api_daily_sales_list_raise_exc(
    fx_kamis_open_api: KamisOpenApi
):
    with Mocker() as m:
        m.get('http://kamis.example.com/example.do', json={}, status_code=500)
        with raises(HTTPError):
            fx_kamis_open_api.daily_sales_list()
        assert len(m.request_history) == 1


def test_kamis_open_api_period_product_list(
    fx_kamis_open_api: KamisOpenApi,
    fx_period_product_list_parameters: PeriodProductListParameters
):
    with Mocker() as m:
        m.get(
            'http://kamis.example.com/example.do',
            json={
                'condition': [
                    {
                        'p_startday': '2020-10-21',
                        'p_endday': '2020-10-22',
                        'p_countycode': [],
                        'p_itemcategorycode': '100',
                        'p_itemcode': '111',
                        'p_kindcode': '01',
                        'p_productrankcode': '04',
                        'p_convert_kg_yn': 'N',
                        'p_id': 'test',
                        'p_key': 'test',
                        'p_returntype': 'json',
                    },
                ],
                'data': {
                    'error_code': '000',
                    'item': [
                        {
                            'countyname': '평균',
                            'itemname': [],
                            'kindname': [],
                            'marketname': [],
                            'price': '58,633',
                            'regday': '10/21',
                            'yyyy': '2020',
                        },
                        {
                            'countyname': '평균',
                            'itemname': [],
                            'kindname': [],
                            'marketname': [],
                            'price': '58,544',
                            'regday': '10/22',
                            'yyyy': '2020',
                        },
                        {
                            'countyname': '평년',
                            'itemname': [],
                            'kindname': [],
                            'marketname': [],
                            'price': '46,112',
                            'regday': '10/21',
                            'yyyy': '2020',
                        },
                        {
                            'countyname': '평년',
                            'itemname': [],
                            'kindname': [],
                            'marketname': [],
                            'price': '46,260',
                            'regday': '10/22',
                            'yyyy': '2020',
                        },
                        {
                            'countyname': '서울',
                            'itemname': '쌀',
                            'kindname': '일반계(20kg)',
                            'marketname': '경동',
                            'price': '57,300',
                            'regday': '10/21',
                            'yyyy': '2020',
                        },
                        {
                            'countyname': '서울',
                            'itemname': '쌀',
                            'kindname': '일반계(20kg)',
                            'marketname': '경동',
                            'price': '58,300',
                            'regday': '10/22',
                            'yyyy': '2020',
                        },
                        {
                            'countyname': '부산',
                            'itemname': '쌀',
                            'kindname': '일반계(20kg)',
                            'marketname': '부전',
                            'price': '60,000',
                            'regday': '10/21',
                            'yyyy': '2020',
                        },
                        {
                            'countyname': '부산',
                            'itemname': '쌀',
                            'kindname': '일반계(20kg)',
                            'marketname': '부전',
                            'price': '60,000',
                            'regday': '10/22',
                            'yyyy': '2020',
                        },
                    ],
                },
            }
        )
        period_product_list = fx_kamis_open_api.period_product_list(
            fx_period_product_list_parameters
        )
        assert period_product_list == PeriodProductListResponse(
            condition=[
                {
                    'p_startday': '2020-10-21',
                    'p_endday': '2020-10-22',
                    'p_countycode': [],
                    'p_itemcategorycode': '100',
                    'p_itemcode': '111',
                    'p_kindcode': '01',
                    'p_productrankcode': '04',
                    'p_convert_kg_yn': 'N',
                    'p_id': 'test',
                    'p_key': 'test',
                    'p_returntype': 'json',
                },
            ],
            data=PeriodProductListDataResponse(
                item=[
                    PeriodProductListItemResponse(
                        countyname='평균',
                        itemname=[],
                        kindname=[],
                        marketname=[],
                        price='58,633',
                        regday='10/21',
                        yyyy='2020'
                    ),
                    PeriodProductListItemResponse(
                        countyname='평균',
                        itemname=[],
                        kindname=[],
                        marketname=[],
                        price='58,544',
                        regday='10/22',
                        yyyy='2020'
                    ),
                    PeriodProductListItemResponse(
                        countyname='평년',
                        itemname=[],
                        kindname=[],
                        marketname=[],
                        price='46,112',
                        regday='10/21',
                        yyyy='2020'
                    ),
                    PeriodProductListItemResponse(
                        countyname='평년',
                        itemname=[],
                        kindname=[],
                        marketname=[],
                        price='46,260',
                        regday='10/22',
                        yyyy='2020'
                    ),
                    PeriodProductListItemResponse(
                        countyname='서울',
                        itemname='쌀',
                        kindname='일반계(20kg)',
                        marketname='경동',
                        price='57,300',
                        regday='10/21',
                        yyyy='2020'
                    ),
                    PeriodProductListItemResponse(
                        countyname='서울',
                        itemname='쌀',
                        kindname='일반계(20kg)',
                        marketname='경동',
                        price='58,300',
                        regday='10/22',
                        yyyy='2020'
                    ),
                    PeriodProductListItemResponse(
                        countyname='부산',
                        itemname='쌀',
                        kindname='일반계(20kg)',
                        marketname='부전',
                        price='60,000',
                        regday='10/21',
                        yyyy='2020'
                    ),
                    PeriodProductListItemResponse(
                        countyname='부산',
                        itemname='쌀',
                        kindname='일반계(20kg)',
                        marketname='부전',
                        price='60,000',
                        regday='10/22',
                        yyyy='2020'
                    ),
                ],
                error_code=ResultCode.SUCCESS.value
            )
        )
        assert len(m.request_history) == 1


def test_kamis_open_api_period_product_list_no_data(
    fx_kamis_open_api: KamisOpenApi
):
    with Mocker() as m:
        m.get(
            'http://kamis.example.com/example.do',
            json={
                'condition': [
                    {
                        'p_startday': '2020-10-21',
                        'p_endday': '2020-10-22',
                        'p_countycode': [],
                        'p_itemcategorycode': '500',
                        'p_itemcode': '514',
                        'p_kindcode': '01',
                        'p_productrankcode': '05',
                        'p_convert_kg_yn': 'N',
                        'p_id': 'test',
                        'p_key': 'test',
                        'p_returntype': 'json',
                    },
                ],
                'data': ['001']
            }
        )
        period_product_list = fx_kamis_open_api.period_product_list(
            PeriodProductListParameters(
                (datetime.date(2020, 10, 21), datetime.date(2020, 10, 22)),
                None, '500', '514', '01', '05', None, None
            )
        )
        assert period_product_list == PeriodProductListResponse(
            condition=[
                {
                    'p_startday': '2020-10-21',
                    'p_endday': '2020-10-22',
                    'p_countycode': [],
                    'p_itemcategorycode': '500',
                    'p_itemcode': '514',
                    'p_kindcode': '01',
                    'p_productrankcode': '05',
                    'p_convert_kg_yn': 'N',
                    'p_id': 'test',
                    'p_key': 'test',
                    'p_returntype': 'json',
                },
            ],
            data=PeriodProductListDataResponse(
                item=[],
                error_code=ResultCode.NO_DATA
            )
        )
        assert len(m.request_history) == 1


def test_kamis_open_api_period_product_list_raise_exc(
    fx_kamis_open_api: KamisOpenApi,
    fx_period_product_list_parameters: PeriodProductListParameters
):
    with Mocker() as m:
        m.get('http://kamis.example.com/example.do', json={}, status_code=500)
        with raises(HTTPError):
            fx_kamis_open_api.period_product_list(
                fx_period_product_list_parameters
            )
        assert len(m.request_history) == 1
