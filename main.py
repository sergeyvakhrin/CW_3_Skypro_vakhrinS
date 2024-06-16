from config import DATA_PATH
from src.product import Product
from src.utils import load_data, get_category_list


def main():

    # загрузка данных
    data = load_data(DATA_PATH)

    # создание списка экземпляров классов категорий товаров
    categories: list = get_category_list(data)


if __name__ == "__main__":
    main()
