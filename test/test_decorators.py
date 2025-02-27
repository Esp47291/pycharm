import pytest

from src.decorators import filter_by_currency, transaction_descriptions, card_number_generator

# Тестовые данные можно использовать те же, что в примере
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
]

def test_filter_by_currency_usd():
    """Тест фильтрации транзакций по валюте USD"""
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]["operationAmount"]["currency"]["code"] == "USD"
    assert usd_transactions[0]["id"] == 939719570

def test_filter_by_currency_rub():
    """Тест фильтрации транзакций по валюте RUB"""
    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 1
    assert rub_transactions[0]["operationAmount"]["currency"]["code"] == "RUB"
    assert rub_transactions[0]["id"] == 873106923

def test_filter_by_currency_empty():
    """Тест фильтрации с несуществующей валютой"""
    eur_transactions = list(filter_by_currency(transactions, "EUR"))
    assert len(eur_transactions) == 0

def test_transaction_descriptions():
    """Тест генерации описаний транзакций"""
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 2
    assert descriptions[0] == "Перевод организации"
    assert descriptions[1] == "Перевод со счета на счет"

def test_transaction_descriptions_empty():
    """Тест генерации описаний для пустого списка"""
    empty_descriptions = list(transaction_descriptions([]))
    assert len(empty_descriptions) == 0

def test_card_number_generator_format():
    """Тест формата генерируемых номеров карт"""
    cards = list(card_number_generator(1234567890123456, 1234567890123456))
    assert len(cards) == 1
    assert cards[0] == "1234 5678 9012 3456"
    assert len(cards[0]) == 19  # 16 цифр + 3 пробела

def test_card_number_generator_sequence():
    """Тест последовательности номеров"""
    cards = list(card_number_generator(1234567890123456, 1234567890123458))
    assert len(cards) == 3
    assert cards[0] == "1234 5678 9012 3456"
    assert cards[1] == "1234 5678 9012 3457"
    assert cards[2] == "1234 5678 9012 3458"

def test_card_number_generator_padding():
    """Тест корректного заполнения нулями"""
    cards = list(card_number_generator(1, 1))
    assert cards[0] == "0000 0000 0000 0001"

@pytest.mark.parametrize("start, end, expected_count", [
    (100, 102, 3),
    (999, 998, 0),
    (500, 500, 1),
])
def test_card_number_generator_range(start, end, expected_count):
    """Параметризованный тест диапазона генерации"""
    cards = list(card_number_generator(start, end))
    assert len(cards) == expected_count

if __name__ == "__main__":
    pytest.main()