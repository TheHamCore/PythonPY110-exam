import json
import random

from faker import Faker

from conf import MODEL

FILE_NAME_READING = 'books.txt'
FILE_NAME_WRITING = 'result.json'

faker = Faker()


def main():
    res = create_dict(1)
    res_array = []
    for i in range(99):  # fixme list comprehension
        data = (next(res))
        res_array.append(data)
    with open(FILE_NAME_WRITING, 'w', encoding='utf-8') as f:
        json.dump(res_array, f, ensure_ascii=False, indent=4)


def create_dict(pk) -> dict:  # todo Iterator[dict]
    while True:
        result_dict = {
            'model': add_model_to_dict(),
            'pk': pk,
            'fields': {
                'title': add_fields_title_to_dict(),  #
                'year': add_fields_year_to_dict(),  #
                'pages': add_fields_pages_to_dict(),
                'isbn13': add_fields_isbn13_to_dict(),
                'rating': add_fields_rating_to_dict(max_value=5),
                'price': add_fields_price_to_dict(min_price=10, max_price=10000),
                'author': [
                    author1(authors=['Alex', 'Jhon', 'Luci']), author2(authors=['Alex', 'Jhon', 'Luci'])
                ],

            }
        }
        yield result_dict
        pk += 1


def add_model_to_dict() -> str:
    """
    :return:
    """
    return MODEL


def add_fields_title_to_dict() -> str:
    with open(FILE_NAME_READING, encoding='utf-8') as f:
        my_fields = f.readlines()
        my_fields = [line.rstrip() for line in my_fields]

        return faker.random_element(elements=my_fields)


def add_fields_year_to_dict() -> int:
    """
    :return:
    """
    return int(faker.year())


def add_fields_pages_to_dict(min_value=10, max_value=9999) -> int:
    """
    :param min_value:
    :param max_value:
    :return:
    """
    return int(faker.random_int(min=min_value, max=max_value))


def add_fields_isbn13_to_dict() -> str:
    """
    :return:
    """
    return faker.isbn13()


def add_fields_rating_to_dict(max_value) -> float:
    """
    :param max_value:
    :return:
    """
    return random.random() * max_value


def add_fields_price_to_dict(min_price, max_price) -> int:
    """
    :param min_price:
    :param max_price:
    :return:
    """
    return random.randint(min_price, max_price)


def author1(authors) -> list[str]:
    return faker.random_element(elements=authors)


def author2(authors) -> list:  # todo убрать
    """
    :param authors:
    :return:
    """
    return faker.random_element(elements=authors)


if __name__ == '__main__':
    main()
