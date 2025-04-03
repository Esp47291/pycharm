from src.transaction_categories import count_operations_by_category


def test_count_operations_by_category():
    transactions = [
        {"description": "Перевод на счет"},
        {"description": "Покупка в магазине"},
        {"description": "Перевод на счет"},
        {"description": "Оплата услуг"},
    ]

    result = count_operations_by_category(transactions)
    assert result["Перевод на счет"] == 2
    assert result["Покупка в магазине"] == 1
    assert result["Оплата услуг"] == 1
