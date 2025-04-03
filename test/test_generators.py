# test_generators.py

import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Фикстура для тестовых данных


@pytest.fixture
def sample_transactions() -> list[dict]:
    return [
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
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
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


#  Тесты для filterbycurrency
def filter_by_currenc(sampletransactions: list[dict], usd_transactions=None) -> None:
    filter_by_currency(sampletransactions)
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    with pytest.raises(StopIteration):
        next(usd_transactions)


# Тесты для transaction_descriptions
def transaction_description(sample_transactions: list[dict]) -> None:
    descriptions = transaction_descriptions()
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    with pytest.raises(StopIteration):
        next(descriptions)


# Тесты для card_number_generator
@pytest.mark.parametrize("start, end, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"])
])
def card_number_generate(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected
