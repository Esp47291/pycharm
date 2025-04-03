import pandas as pd

def read_csv(file_path):
    """
    Читает данные из CSV-файла и возвращает их в виде DataFrame.

    :param file_path: Путь к файлу CSV.
    :return: pandas.DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return None


def read_excel(file_path):
    """
    Читает данные из Excel-файла и возвращает их в виде DataFrame.

    :param file_path: Путь к файлу Excel.
    :return: pandas.DataFrame
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return None