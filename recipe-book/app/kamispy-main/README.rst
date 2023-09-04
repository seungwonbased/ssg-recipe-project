Kamispy
=======

KAMIS Open-API의 비공식 파이썬 클라이언트입니다.

다음의 API 문서를 읽어주세요:

https://www.kamis.or.kr/customer/reference/openapi_list.do


요구사항
~~~~~~~~

- Python 3.7 이상

- KAMIS Open-API 인증 키

  - KAMIS 홈페이지에서 발급받을 수 있습니다.

    https://www.kamis.or.kr/customer/reference/openapi_write.do


면책조항
~~~~~~~~

이 프로젝트는 스포카에서 제공하는 KAMIS Open-API의 비공식 파이썬
클라이언트입니다.  모든 KAMIS Open-API의 API 지원과 동작을 보장하지 않습니다.



지원하는 API 목록
-----------------

Kamispy는 아직 정식 버전이 아니며, 내부적인 필요에 의해 지원하는 API를
추가하고 있습니다.  2020년 12월 9일 기준 지원하는 API 목록은 다음과 같습니다.

- 일별 품목별 도·소매가격정보

- 최근일자 도.소매가격정보(상품 기준)

또한, 아직 지원하지 않는 API 목록은 다음과 같습니다.

- 일별 부류별 도.소매가격정보

- 월별 도.소매가격정보

- 연도별 도.소매가격정보

- 친환경농산물 가격정보

- 최근 가격추이 조회(상품 기준)

- 월평균 가격추이 조회(상품 기준)

- 연평균 가격추이 조회(상품 기준)

- 최근일자 지역별 도.소매가격정보(상품 기준)

- 친환경농산물 품목별 가격정보

- 친환경농산물 가격정보

- 친환경농산물 품목별가격정보

- 지역별 품목별 도.소매가격정보


실행 방법
~~~~~~~~~

클라이언트 초기화 방법
----------------------

클라이언트는 다음과 같이 초기화합니다.  ``cert_key`` 파리미터에는 KAMIS
Open-API 인증 키를 넣고, ``cert_id`` 파라미터에는 KAMIS 홈페이지 계정 아이디를
넣습니다.

.. code-block:: pycon

    >>> from kamis.client import CertificationPair, KamisOpenApi
    >>> client = KamisOpenApi(
    ...     CertificationPair(cert_key='test', cert_id='test')
    ... )


API 실행 예제
-------------

다음은 '최근일자 도.소매가격정보(상품 기준) API'를 실행하는 예제를 보여줍니다.
초기화한 클라이언트에서 ``daily_sales_list`` 함수를 실행합니다.  실행해야 하는
함수의 이름은 각 API의 action 파라미터의 이름과 같습니다.

.. code-block:: pycon

    >>> daily_sales_list = client.daily_sales_list()
    >>> daily_sales_list.result_code
    <ResultCode.SUCCESS: '000'>
    >>> daily_sales_list.prices[0]
    PriceResponse(product_class=<ProductClass.RETAIL: '01'>, category_code='100', category_name='식량작물', productno='272', latest_date=datetime.date(2020, 10, 16), product_name='쌀/일반계', item_name='쌀/일반계', unit='20kg', date_price_dict=OrderedDict([('당일', 55094), ('1일전', 55053), ('1개월전', 52723), ('1년전', 51034)]), direction_type=<Direction.INCREASE: '1'>, direction_value=0.1)
    >>> daily_sales_list.prices[1]
    PriceResponse(product_class=<ProductClass.RETAIL: '01'>, category_code='100', category_name='식량작물', productno='273', latest_date=datetime.date(2020, 10, 16), product_name='쌀/햇일반계', item_name='쌀/햇일반계', unit='20kg', date_price_dict=OrderedDict([('당일', 58887), ('1일전', 58939), ('1개월전', None), ('1년전', 53015)]), direction_type=<Direction.DECREASE: '0'>, direction_value=0.1)


파라미터가 있는 API 실행 예제
-----------------------------

다음은 '일별 품목별 도·소매가격정보 API'를 실행하는 예제를 보여줍니다.

이 API는 인증 정보 외에도 추가적인 파라미터가 필요한데, 이러한 경우 파라미터를
담을 수 있는 ``Parameters`` 클래스가 ``kamis.models`` 하위의 해당하는 API
모듈 내부에 정의되어 있습니다.

.. code-block:: pycon

    >>> from kamis.models.period_product_list import Parameters
    >>> import datetime
    >>> params = Parameters(
    ...     date_range=(
    ...         datetime.date(2020, 10, 21), datetime.date(2020, 10, 22)
    ...     ),
    ...     product_class=None,
    ...     item_category_code="100",
    ...     item_code="111",
    ...     kind_code"01",
    ...     product_rank_code="04",
    ...     country=None,
    ...     convert_kg=None
    ... )

파라미터를 생성하여 이전 예제와 같이 클라이언트에서 API에 해당하는 함수를
실행합니다.

.. code-block:: pycon

    >>> period_product_list = client.period_product_list(params)
    >>> period_product_list.data.result_code
    <ResultCode.SUCCESS: '000'>
    >>> period_product_list.data.items[0]
    ItemResponse(item_name=None, kind_name=None, county_name='평균', market_name=None, reg_date=datetime.date(2020, 10, 21), price_=54520)
    >>> period_product_list.data.items[1]
    ItemResponse(item_name=None, kind_name=None, county_name='평균', market_name=None, reg_date=datetime.date(2020, 10, 22), price_=54520)
    >>> period_product_list.data.items[4]
    ItemResponse(item_name='쌀', kind_name='일반계(20kg)', county_name='서울', market_name='양곡도매', reg_date=datetime.date(2020, 10, 21), price_=53300)
