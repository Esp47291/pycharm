import csv


def read_transactions_from_csv(file_path):
    """
    Считывает финансовые операции из CSV-файла и возвращает их в виде списка словарей.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        list[dict]: Список словарей, где каждый словарь представляет одну транзакцию.
    """
    transactions = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            # Указываем разделитель (например, запятую). Если разделитель другой, его нужно указать явно.
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                transactions.append(row)
        return transactions
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []
