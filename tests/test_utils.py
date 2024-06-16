from src.utils import get_category_list, load_data


def test_get_category_list(data_json):
    categories = get_category_list(data_json)
    assert len(categories) == 2
    assert len(categories[0].products) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
