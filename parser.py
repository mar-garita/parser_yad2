import requests
from bs4 import BeautifulSoup
import typing

from time import sleep
from random import uniform


class Not200StatusCode(Exception):
    pass


class Parser:
    """
    Basic yad2.co.il parser, data parsing (apartment rentals) for the specified parameters
    Makes request to the site, parses the data, saves data to a list
    """
    base_url = 'https://www.yad2.co.il/realestate/rent?city=5000&property=1'
    rooms_url = '&rooms='
    price_url = '--1&price=-1-'
    floor_url = '&floor='
    end_url = '--1'
    pages_url = '&page={page_number}'

    def __init__(self, keywords, is_paginate=True, url=True):
        self.keywords = keywords
        self.is_paginate = is_paginate
        self.url = url
        self.data = []

    def _make_url(self, keywords: list) -> str:
        """
        Generates a url based on parsing parameters.
        :param keywords: numbers of rooms, price, floor
        :return: url ready for parsing
        """
        # Adds url's with keywords to the base url
        self.url = self.base_url + self.rooms_url + str(keywords[0]) \
                   + self.price_url + str(keywords[1]) \
                   + self.floor_url + str(keywords[2]) + self.end_url
        return self.url

    def _pagination(self, page_number, pages_url):
        """
        Generates the url of the next page and sends a request to the site.
        :param page_number:
        :return: content html
        """
        url = self._make_url(keywords=self.keywords)
        url_pagination = url + pages_url.format(page_number=page_number)
        response = requests.get(url_pagination)
        return response.content

    def _pars_block(self, blocks) -> typing.List[dict]:
        """
        Splits the page content into blocks
        Generates a dictionary for each data block and saves them to a list.
        :param blocks: the content of the page
        :return: list of data
        """
        sleep(uniform(5, 8))
        data = []
        for block in blocks:
            adress_block = block.find('div', class_='rows')
            rooms_floor_area_block = block.find('div', class_='middle_col')
            price_block = block.find('div', class_='price')
            date_added_block = block.find('span', class_='date')

            d = {
                'adress': adress_block.get_text(),
                'rooms_floor_area': rooms_floor_area_block.get_text(),
                'price': price_block.get_text(),
                'date_added': date_added_block.get_text(),
            }

            data.append(d)
        return data

    def parse_content(self, content: bytes, page_number=2) -> typing.List[dict]:
        """
        Recursive method.
        Gets content (blocks), parser it and saves the information to a list.
        Checks for pagination, parses the following pages.
        :param page_number:
        :param content: html
        :return: list of data
        """
        sleep(uniform(8, 15))

        soup = BeautifulSoup(content, 'lxml')

        blocks = soup.find_all('div', class_='feed_item feed_item-v4 accordion desktop')

        data = self._pars_block(blocks)
        self.data.extend(data)
        print('INFO: already parsed {} blocks'.format(len(self.data)))

        # find the button 'next' that is not active in the pagination
        paginated_block = soup.find('div', class_='pagination clickable')
        button_next = paginated_block.find('button', class_='page-num current-page-num')
        print('Next button: ', button_next)  # None

        # if pagination is enabled and button next is active
        if self.is_paginate and not button_next:
            sleep(uniform(8, 15))
            print('INFO: Try to paginate page number ', page_number)
            # get the content of the next page
            content = self._pagination(page_number, pages_url=self.pages_url)

            self.parse_content(content, page_number + 1)

        return self.data

    def send_request(self, url: str) -> bytes:
        """
        The method generates and sends a request to the site.
        Calls the sleep method to avoid being banned.
        :param url: url with search parameters
        :return: html content
        """
        sleep(uniform(3, 8))

        print('INFO: url is ', url)

        response = requests.get(url)

        if not response.status_code == 200:
            raise Not200StatusCode('Status code is: ', response.status_code)

        print('INFO: Status code is 200')
        # print(response.content)

        return response.content

    def start(self, keywords: list):
        """
        Calls methods of the class.
        :param keywords: numbers of rooms, price, floor
        :return:
        """
        url = self._make_url(keywords)
        html_content = self.send_request(url)

        print(html_content)  # Если забанили, показывает капчу

        data = self.parse_content(html_content)
        print('LEN DATA: ', len(data))

        return data