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
        product_str = ""
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

