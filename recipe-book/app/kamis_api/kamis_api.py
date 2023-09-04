from kamis.client import CertificationPair, KamisOpenApi


client = KamisOpenApi(
    CertificationPair(
        cert_key="8e048ef8-d021-43d2-9810-d7be607879e4", cert_id="oreobae@ajou.ac.kr"
    )
)


daily_sales_list = client.daily_sales_list()
info = dict()


def get_info():
    for i in range(215):
        info[daily_sales_list.prices[i].productName] = [daily_sales_list.prices[i].date_price_dict["당일"],
                                                        daily_sales_list.prices[i].unit]

    return info


test = get_info()

for key, val in test.items():
    print(key, val)
