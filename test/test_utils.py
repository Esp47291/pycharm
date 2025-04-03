import os
import json
import tempfile
from unittest import mock

import pytest

from src.utils import read_json_file
from src.external_api import convert_to_rub
import requests
import json


def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка парсинга JSON: {file_path}")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return []


def test_read_json_file():
    # Тест: чтение корректного JSON-файла
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        data = [{"id": 1, "description": "Test transaction"}]
        json.dump(data, temp_file)
        temp_file_path = temp_file.name

    result = read_json_file(temp_file_path)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["id"] == 1
    os.unlink(temp_file_path)

    # Тест: чтение несуществующего файла
    result = read_json_file("nonexistent_file.json")
    assert result == []

    # Тест: чтение поврежденного JSON-файла
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("invalid json")
        temp_file_path = temp_file.name

    result = read_json_file(temp_file_path)
    assert result == []
    os.unlink(temp_file_path)


from unittest import mock
from src.external_api import convert_to_rub


def test_convert_to_rub():
    # Тест: успешная конвертация USD в RUB
    transaction = {'currency': 'USD', 'amount': 100}
    with mock.patch('src.external_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rates': {'RUB': 75}
        }
        result = convert_to_rub(transaction)
        assert result == 7500.0

    # Тест: ошибка API
    with mock.patch('src.external_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {}
        result = convert_to_rub(transaction)
        assert result == 0.0

    # Тест: валюта не требует конвертации
    transaction = {'currency': 'RUB', 'amount': 5000}
    result = convert_to_rub(transaction)
    assert result == 5000


import logging

logging.basicConfig(level=logging.DEBUG)


def convert_to_rub(transaction):
    if transaction['currency'] == 'RUB':
        return transaction['amount']

    if transaction['currency'] == 'USD':
        try:
            logging.debug("Выполняется запрос к API...")
            response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
            response.raise_for_status()
            rate = response.json().get('rates', {}).get('RUB', 1)
            return transaction['amount'] * rate
        except requests.RequestException as e:
            logging.error(f"Ошибка при запросе к API: {e}")
            return 0.0

    return 0.0

@pytest.fixture
def mock_requests_get():
    with mock.patch('src.external_api.requests.get') as mock_get:
        yield mock_get
