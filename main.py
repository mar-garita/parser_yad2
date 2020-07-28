from parser import Parser
from save_data import Pipeline, create_db

"""
Main part - launch all
"""

# List of url parameters
KEYWORDS = [
    {'rooms': 3},
    {'price': 4000},
    {'floor': 2}
]

list_keywords = []

# Creating a list of values
for dic in KEYWORDS:
    for keyword in dic.values():
        list_keywords.append(keyword)


def main():
    parser = Parser(keywords=list_keywords, is_paginate=False)
    data = parser.start(list_keywords)
    Pipeline(data).save_data()


if __name__ == '__main__':
    create_db()
    main()