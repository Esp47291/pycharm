from unittest import mock
from utils import read_json_file
from external_api import convert_to_rub


def test_read_json_file():
    # Пример теста, когда файл существует и содержит список
    result = read_json_file("data/operations.json")
    assert isinstance(result, list)

    # Пример теста, когда файл пустой или не существует
    result = read_json_file("data/nonexistent_file.json")
    assert result == []


def test_convert_to_rub():
    transaction = {'currency': 'USD', 'amount': 100}

    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'result': 75.0}
        result = convert_to_rub(transaction)
        assert result == 75.0
