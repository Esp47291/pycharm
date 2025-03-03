# src/decorators.py

def generator_decorator(func):
    """
    Простой декоратор, который оборачивает
    исходную функцию-генератор и возвращает генератор.
    Здесь можно добавить любую дополнительную логику,
    например логирование.
    """
    def wrapper(*args, **kwargs):
        # возвращаем сам генератор, чтобы сохранилось поведение yield
        return func(*args, **kwargs)
    return wrapper


@generator_decorator
def filter_by_currency(transactions, currency_code):
    """
    Генератор, фильтрующий транзакции по коду валюты.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


@generator_decorator
def transaction_descriptions(transactions):
    """
    Генератор, возвращающий описания транзакций.
    """
    for transaction in transactions:
        yield transaction["description"]


@generator_decorator
def card_number_generator(start, end):
    """
    Генератор, формирующий номера карт в формате:
    'XXXX XXXX XXXX XXXX', заполняя нулями слева при необходимости.
    """
    for number in range(start, end + 1):
        card_number = str(number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"