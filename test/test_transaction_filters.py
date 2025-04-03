from src.transaction_filters import filter_by_description


def test_filter_by_description():
    transactions = [
        {"id": 1, "description": "Перевод на счет"},
        {"id": 2, "description": "Покупка в магазине"},
        {"id": 3, "description": "Перевод между счетами"},
    ]

    result = filter_by_description(transactions, "перевод")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3
