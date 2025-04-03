import pandas as pd


def read_csv(file_path):
    try:
        # Попытка прочитать CSV-файл
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Файл пустой")
        return None
    except pd.errors.ParserError:
        print("Ошибка парсинга CSV")
        return None
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return None


def read_excel(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return None
