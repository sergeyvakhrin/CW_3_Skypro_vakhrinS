import json

from src.category import Category
from src.product import Product


def load_data(path) -> list[dict]:
    """ Загрузка данных из файла """
    with open(path, "rt", encoding="UTF-8") as file:
        return json.load(file)


def get_category_list(data) -> list:
    """ Создание экземпляров классов """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


