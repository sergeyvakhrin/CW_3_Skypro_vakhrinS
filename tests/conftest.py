import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(name="Samsung Galaxy C23 Ultra",
                   description="256GB, Серый цвет, 200MP камера",
                   price=180000.0,
                   quantity=5)


@pytest.fixture
def category1():
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                    products=[
                        Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
                        Product("Iphone 15", "512GB, Gray space", 210000.0, 5),
                        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
                    ])


@pytest.fixture
def category2():
    return Category(name="Телевизоры",
                    description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                    products=[
                        Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7),
                              ])


@pytest.fixture
def data_json():
    return [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [  {"name": "Samsung Galaxy C23 Ultra", "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5},
                       {"name": "Samsung Galaxy C23 Ultra", "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5}
                       ]
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [  {"name": "55 QLED 4K", "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}]
    }
    ]
