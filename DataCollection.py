from SearchStringUtility import SearchStringUtility
from bs4 import BeautifulSoup
import json
import requests
import datetime

class DataCollection:
    search_term = ""
    def __init__(self):
        pass

    def get_data(self, search_url):
        self.search_url = search_url
        agent = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        page_data = requests.get(search_url, headers=agent)
        page_idx = 1
        soup = BeautifulSoup(page_data.text, "html.parser")
        all_items = soup.find_all('div', class_='list-item')
        final_data = []
        for item in all_items:
            try:
                attribute_list = item.attrs
                name = "".join(attribute_list['data-name'].split("-"))
                sku_id = attribute_list['data-sku-id']
                price = json.loads(attribute_list['data-price-json'])
                current_price = price['currentPrice']
                brand_dict = json.loads(attribute_list['data-brand'])
                brand = brand_dict['brand']
                avg_rating = attribute_list['data-average-rating']
                num_reviews = attribute_list['data-review-count']
                current_date = datetime.datetime.today().strftime('%Y-%m-%d')
                data_obj = {
                    "date": current_date,
                    "sku-id" : sku_id,
                    "name" : name,
                    "curr_price" : current_price,
                    "brand" : brand,
                    "avg_rating" : avg_rating,
                    "num_ratings" : num_reviews
                }

                final_data.append(data_obj)

            except AttributeError:
                print("Problem")

        return final_data


# url = 'https://www.bestbuy.com/site/searchpage.jsp?st=curved+smart+tv&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'
# dc = DataCollection()
# print(dc.get_data(url))