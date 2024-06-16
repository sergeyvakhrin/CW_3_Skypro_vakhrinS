import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product(name="Samsung Galaxy C23 Ultra",
                   description="256GB, Серый цвет, 200MP камера",
                   price=180000.0,
                   quantity=5)