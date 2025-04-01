import pandas as pd


def read_transactions_from_excel(file_path):
    """
    Считывает финансовые операции из Excel-файла и возвращает их в виде списка словарей.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        list[dict]: Список словарей, где каждый словарь представляет одну транзакцию.
    """
    try:
        # Читаем Excel-файл с помощью pandas
        df = pd.read_excel(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []
