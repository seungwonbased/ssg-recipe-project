from kamisclient.client import CertificationPair, KamisOpenApi
from app.models import Food
from app import db


client = KamisOpenApi(
    CertificationPair(
        cert_key="8e048ef8-d021-43d2-9810-d7be607879e4", cert_id="oreobae@ajou.ac.kr"
    )
)


# API 호출
daily_sales_list = client.daily_sales_list()
info = dict()
food = Food()


# 데이터 Parsing
def get_food():
    # 215개 한정
    for i in range(215):
        """sumary_line
        카테고리가 축산물, 수산물일 경우와 나머지일 경우를 나눠 파싱
        """
        if daily_sales_list.prices[i].category_code in ("500", "600"):
            name = daily_sales_list.prices[i].product_name

            info[name] = [
                daily_sales_list.prices[i].date_price_dict["당일"],
                daily_sales_list.prices[i].unit,
                daily_sales_list.prices[i].category_name,
                daily_sales_list.prices[i].category_code,
            ]
        else:
            name = daily_sales_list.prices[i].product_name.split("/")

            info[name[0]] = [
                daily_sales_list.prices[i].date_price_dict["당일"],
                daily_sales_list.prices[i].unit,
                daily_sales_list.prices[i].category_name,
                daily_sales_list.prices[i].category_code,
            ]

    return info


parsed_data = get_food()


# DB에 삽입
for key, val in parsed_data.items():
    food(key, val)
    db.session.add(food)
