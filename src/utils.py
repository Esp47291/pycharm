from src.external_api import convert_to_rub

import requests


def convert_to_rub(transaction):
    # Если валюта уже в RUB, возвращаем сумму без изменений
    if transaction['currency'] == 'RUB':
        return transaction['amount']

    # Если валюта USD, пытаемся получить курс через API
    if transaction['currency'] == 'USD':
        try:
            response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
            response.raise_for_status()  # Проверка статуса ответа
            rate = response.json().get('rates', {}).get('RUB', 1)  # Получаем курс RUB
            return transaction['amount'] * rate
        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return 0.0  # Возвращаем 0.0 при ошибке

    # Если валюта не поддерживается, возвращаем 0.0
    return 0.0


def read_json_file():
    return None
