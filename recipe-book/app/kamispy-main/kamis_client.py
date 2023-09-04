from kamis.client import CertificationPair, KamisOpenApi


client = KamisOpenApi(
    CertificationPair(
        cert_key='8e048ef8-d021-43d2-9810-d7be607879e4', cert_id='3619'
    )
)

daily_sales_list = client.daily_sales_list()
print(daily_sales_list.result_code)
