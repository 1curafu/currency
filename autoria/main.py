import csv
from bs4 import BeautifulSoup
import requests
import random
from time import sleep
import sqlite3


def random_sleep():
    sleep(random.randint(1, 5))

direct = (
    'car_id', 'data_link_to_view', 'car_price', 'salesman_name', 'car_brand_model_year',
    'car_motor', 'car_color'
)

def get_page_content(page: int, size: int = 100) -> str:
    query_parameters = {
        'indexName': 'auto,order_auto,newauto_search',
        'country.import.usa.not': '-1',
        'price.currency': '1',
        'abroad.not': '-1',
        'custom.not': '-1',
        'page': page,
        'size': size
    }
    base_url = 'https://auto.ria.com/search/'
    response = requests.get(base_url, params=query_parameters)
    response.raise_for_status()
    return response.text


def get_detail_content(link: str) -> str:
    base_url = 'https://auto.ria.com/uk'
    url = base_url + link
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def create_car_list(car_id: str, link: str, price: int, name: str, dictionary: list) -> list:
    car_direct = (
        'car_brand_model_year', 'car_motor', 'car_color'
    )

    car_inform = dict(zip(car_direct, dictionary))

    car_brand_model_year = car_inform.get('car_brand_model_year')
    car_motor = car_inform.get('car_motor')
    car_color = car_inform.get('car_color')

    cars_data = [car_id, link, price, name, car_brand_model_year, car_motor, car_color]
    return cars_data

class CSVWriter:
    
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers
        
        with open(self.filename, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
    
    def write(self, row: list):
        with open(self.filename, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)
        
class StdOutWriter:
    def write(self, row: list):
        print(row) # noqa

class SQLiteWriter:
    def __init__(self, db_name):
        self.db_name = db_name

        with sqlite3.connect(self.db_name) as data_base:
            cur = data_base.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS cars(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_id INTEGER,
                data_link_to_view NVARCHAR(80),
                car_price INTEGER,
                salesman_name NVARCHAR(80),
                car_brand_model_year NVARCHAR(80),
                car_motor NVARCHAR(40),
                car_color NVARCHAR(20))
            """)
            data_base.commit()

    def write(self, row: list):
        connection = sqlite3.connect(self.db_name)
        cur = connection.cursor()
        insert_data = """INSERT INTO cars(car_id, data_link_to_view, car_price, salesman_name,
                          car_brand_model_year, car_motor, car_color)
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

        cur.execute(insert_data, row)
        connection.commit()

        cur.close()

def main():
    
    writers = (
        CSVWriter('cars.csv', direct),
        CSVWriter('cars2.csv', direct),
        StdOutWriter(),
        SQLiteWriter('cars_info.db')
    )
    
    page = 2514
    

    while True:
        
        
        print(f"Page: {page}")
        
        page_content = get_page_content(page)
        
        page += 1
        
        soup = BeautifulSoup(page_content, features="html.parser")
    
        search_results = soup.find("div", {"id": "searchResults"})
        ticket_items = search_results.find_all("section", {"class": "ticket-item"})

        if not ticket_items:
            break
        
        
        for ticket_item in ticket_items:
            car_details = ticket_item.find("div", {"class": "hide"})
            car_id = car_details['data-id']
            data_link_to_view = car_details['data-link-to-view']
            
            main_text = get_detail_content(data_link_to_view)

            soup_detail = BeautifulSoup(main_text, features="html.parser")
            search = soup_detail.find("div", {"class": "technical-info ticket-checked"})
            car_params = list()
            
            try:
                search_info = search.findAll("span", {"class": "argument"})
                for item in search_info:
                    car_params.append(item.text)
            except AttributeError:
                pass # noqa

            search_detail = soup_detail.find("div", {"class": "auto-wrap"})
            search_price = search_detail.find("div", {"class": "price_value"})
            search_name = search_detail.find("div", {"class": "seller_info_name bold"})


            price = ''.join(x for x in search_price.text if x.isdigit())
            if search_name:
                name = search_name.text
            else:
                name = None
            


            cars_data = create_car_list(car_id, data_link_to_view, price, name, car_params)

            for writer in writers:
                writer.write(cars_data)



if __name__ == '__main__':
    main()
    

# With the help of the beautifulsoup4 library,you must add parsing of details on the ad from this site: https://auto.ria.com/search/. Record data in csv and sqlite3
