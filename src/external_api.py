from unittest import mock
import pytest
from src.external_api import convert_to_rub


def test_convert_to_rub():
    # Тест 1: Успешная конвертация USD в RUB
    transaction = {'currency': 'USD', 'amount': 100}
    with mock.patch('requests.get') as mock_get:
        # Настройка мока для успешного ответа API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'result': 7500.0  # Курс USD к RUB = 75
        }
        result = convert_to_rub(transaction)
        assert result == 7500.0  # 100 * 75 = 7500

    # Тест 2: Ошибка API (например, статус 400)
    with mock.patch('requests.get') as mock_get:
        # Настройка мока для ошибочного ответа API
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {}
        result = convert_to_rub(transaction)
        assert result == 0.0  # При ошибке API возвращается 0.0

    # Тест 3: Валюта уже в RUB (нет необходимости в конвертации)
    transaction = {'currency': 'RUB', 'amount': 5000}
    result = convert_to_rub(transaction)
    assert result == 5000  # Сумма в RUB остается без изменений

    # Тест 4: Неподдерживаемая валюта (например, EUR)
    transaction = {'currency': 'GBP', 'amount': 200}
    result = convert_to_rub(transaction)
    assert result == 200  # Для неподдерживаемых валют сумма не меняется

    # Тест 5: Исключение при запросе к API
    with mock.patch('requests.get') as mock_get:
        # Имитация исключения при вызове requests.get
        mock_get.side_effect = Exception("Ошибка сети")
        result = convert_to_rub({'currency': 'USD', 'amount': 100})
        assert result == 0.0  # При исключении возвращается 0.0


def convert_to_rub():
    return None