from src.product import Product


class Category:
    """ Класс категорий товаров """
    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

