import requests


headers = {"Authorization": "Bearer 45b6a809-f1aa-48d6-a7f4-93dc08a227bc"}
x = requests.get('https://ajiobusiness.com/rrlmpcommercewebservices/v2/rrlmp/cms/pdp/pagedata?pageId=ProductDetailPage&pageType=productDetailsPage&productCode=461551147&page_ref=plp&brand=GRUBSTAKER&page_ref=plp',headers=headers,params={'type':'CREDIT30DAYS'})

print(x.content)
print(x.request)
print(x.links)