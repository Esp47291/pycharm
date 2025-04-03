import json
import csv
import pandas as pd
from src.transaction_filters import filter_by_description


def load_json_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Ошибка при чтении JSON-файла: {e}")
        return []


def load_csv_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []


def load_excel_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df.to_dict('records')
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []


def print_transaction(transaction):
    """Выводит информацию о транзакции."""
    date = transaction.get("date", "Дата не указана")
    description = transaction.get("description", "Описание отсутствует")
    amount = transaction.get("amount", "Сумма не указана")
    currency = transaction.get("currency", "Валюта не указана")
    print(f"{date} {description}")
    print(f"Сумма: {amount} {currency}\n")


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Введите номер пункта: ")
    if choice not in ["1", "2", "3"]:
        print("Некорректный выбор. Попробуйте снова.")
        return

    if choice == "1":
        transactions = load_json_data("data/transactions.json")
    elif choice == "2":
        transactions = load_csv_data("data/transactions.csv")
    else:
        transactions = load_excel_data("data/transactions.xlsx")

    if not transactions:
        print("Не удалось загрузить данные.")
        return

    status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()
    while status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print("Статус операции недоступен.")
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()

    filtered_transactions = [t for t in transactions if t.get("state", "").upper() == status]

    sort_by_date = input("Отсортировать операции по дате? Да/Нет: ").lower() == "да"
    if sort_by_date:
        order = input("По возрастанию или по убыванию? Введите 'возрастание' или 'убывание': ").lower()
        reverse = order == "убывание"
        filtered_transactions.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    rub_only = input("Выводить только рублевые транзакции? Да/Нет: ").lower() == "да"
    if rub_only:
        filtered_transactions = [t for t in filtered_transactions if t.get("currency", "") == "RUB"]

    filter_description = input("Отфильтровать по описанию? Да/Нет: ").lower() == "да"
    if filter_description:
        search_string = input("Введите строку для поиска: ")
        filtered_transactions = filter_by_description(filtered_transactions, search_string)

    print("\nРаспечатываю итоговый список транзакций...")
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print_transaction(transaction)


if __name__ == "__main__":
    main()
