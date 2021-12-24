import json
import random
from typing import Iterator

from faker import Faker

from conf import MODEL

from typing import List

FILE_NAME_READING = 'books.txt'
FILE_NAME_WRITING = 'result.json'

faker = Faker()


def main():
    """Creating .json file with data"""
    result_dict = create_dict(pk=1)

    list_of_objects = []
    for i in range(100):
        dict_of_objects = {key: value for key, value in next(result_dict).items()}
        list_of_objects.append(dict_of_objects)

    with open(FILE_NAME_WRITING, 'w', encoding='utf-8') as f:
        json.dump(list_of_objects, f, ensure_ascii=False, indent=4)


def create_dict(pk) -> Iterator[dict]:
    """
    :param pk: (int) autoincrement integer which increase while new object generation
    :return: Iterator[dict]
    """
    while True:
        result_dict = {
            'model': add_model_to_dict(),
            'pk': pk,
            'fields': {
                'title': add_fields_title_to_dict(),
                'year': add_fields_year_to_dict(),
                'pages': add_fields_pages_to_dict(),
                'isbn13': add_fields_isbn13_to_dict(),
                'rating': add_fields_rating_to_dict(),
                'price': add_fields_price_to_dict(),
                'author': author(authors=['Michael', 'Aria', 'Lamar', 'Alex', 'Jon', 'Luci'])
            }
        }

        yield result_dict

        pk += 1


def add_model_to_dict() -> str:
    """
    :return: (str) string value from file conf.py
    """
    return MODEL


def add_fields_title_to_dict() -> List[str]:
    """
    :return: (list[str]) list of values from FILE_NAME_READING
    """
    with open(FILE_NAME_READING, encoding='utf-8') as f:
        my_fields = f.readlines()
        my_fields = [line.rstrip() for line in my_fields]
        return faker.random_element(elements=my_fields)


def add_fields_year_to_dict() -> int:
    """
    :return: (int) random years
    """
    return int(faker.year())


def add_fields_pages_to_dict(min_value: int = 10, max_value: int = 9999) -> int:
    """
    :param min_value: (int) minimum value integer of pages
    :param max_value: (int) maximum value integer of pages
    :return: (int) random value of integer between minimum value and maximum value
    """
    return int(faker.random_int(min=min_value, max=max_value))


def add_fields_isbn13_to_dict() -> str:
    """
    :return: (str) isbn for book
    """
    return faker.isbn13()


def add_fields_rating_to_dict(max_value: int = 5) -> float:
    """
    :param max_value: (int) maximum floating point number of range(0, 5)
    :return: (float) random floating point number
    """
    return random.random() * max_value


def add_fields_price_to_dict(min_price: int = 10, max_price: int = 10000) -> int:
    """
    :param min_price: (int) minimum price in range of price
    :param max_price: (int) maximum price in range of price
    :return: (int) random integer from this range
    """
    return random.randint(min_price, max_price)


def author(authors) -> List[str]:
    """
    :param authors: list which contains names
    :return: random value from list
    """
    return faker.random_elements(elements=authors, length=random.randrange(1, 4), unique=True)


if __name__ == '__main__':
    main()
