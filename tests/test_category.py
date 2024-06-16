def test_category_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert len(category1.products) == 3
    assert len(category2.products) == 1
    assert category1.category_count == 2
    assert category1.product_count == 4
