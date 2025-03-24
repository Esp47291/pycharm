import requests
import os
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: Dict) -> float:
    if transaction['currency'] in ['USD', 'EUR']:
        amount = transaction['amount']
        base_currency = transaction['currency']
        response = requests.get(
            API_URL,
            params={
                "from": base_currency,
                "to": "RUB",
                "amount": amount,
                "apikey": API_KEY
            }
        )
        data = response.json()
        return data.get('result', 0.0)
    return transaction['amount']
