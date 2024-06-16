class Product:
    """ Класс продуктов """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict):
        name, description, price, quantity = product.values()
        return cls(name, description, price, quantity)
