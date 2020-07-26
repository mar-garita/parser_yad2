from parser import Parser


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
    for val in dic.values():
        list_keywords.append(val)


def main():
    parser = Parser(keywords=list_keywords, is_paginate=False)
    data = parser.start(list_keywords)


if __name__ == '__main__':
    main()