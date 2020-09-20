from parser import Parser
from save_data import Pipeline, create_db
from settings import ROOMS, PRICE, FLOOR

"""
Main part - launch all
"""

# List of url parameters
KEYWORDS = [
    {'rooms': ROOMS},
    {'price': PRICE},
    {'floor': FLOOR}
]

list_keywords = []

# Creating a list of values
for dic in KEYWORDS:
    for keyword in dic.values():
        list_keywords.append(keyword)


def main():
    parser = Parser(keywords=list_keywords, is_paginate=True)
    data = parser.start(list_keywords)
    Pipeline(data).save_data()


if __name__ == '__main__':
    create_db()
    main()