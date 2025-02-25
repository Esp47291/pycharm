
# generators.py

from typing import Dict, List, Iterator, Generator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список транзакций.
    :param currency: Код валюты для фильтрации.
    :return: Итератор, возвращающий транзакции с указанной валютой.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Генерирует описания транзакций.

    :param transactions: Список транзакций.
    :return: Генератор, возвращающий описания транзакций.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генерирует номера банковских карт в заданном диапазоне.

    :param start: Начальное значение диапазона.
    :param end: Конечное значение диапазона.
    :return: Генератор, возвращающий номера карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
                                                                         8:12] + " " + f"{number:016d}"[12:16]
