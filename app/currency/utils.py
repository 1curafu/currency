from decimal import Decimal
from bs4 import BeautifulSoup

import requests


def to_2_places_decimal(value: str) -> Decimal:
    '''
    Convert str value to Decimal with 2 places
        example:
        '123.456' -> Decimal('123.45')
    '''
    return round(Decimal(value), 2)


def parse_oschad_rates(url: str = 'https://www.oschadbank.ua/currency-rate') -> list[dict]:

    response = requests.get(url).text

    soup = BeautifulSoup(response, 'html.parser')

    rates = soup.find_all('tr', class_='heading-block-currency-rate__table-row')

    keys = [td.text for td in rates[0].find_all('td')]

    rate_dict = [{k: td.text for k, td in zip(keys, rate.find_all('td'))} for rate in rates[1:8]]

    return rate_dict
