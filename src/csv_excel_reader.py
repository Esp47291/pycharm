import pandas as pd

def read_transactions_csv(file_path):
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        list[dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []

def read_transactions_excel(file_path):
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        list[dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []
