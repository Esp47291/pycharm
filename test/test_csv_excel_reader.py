import pandas as pd
import pytest
from src.csv_excel_reader import read_csv, read_excel
from tempfile import NamedTemporaryFile


def test_read_csv():
    test_data = "id,name,value\n1,Alice,100\n2,Bob,200"

    with NamedTemporaryFile(mode='w+', delete=False, suffix='.csv', encoding='utf-8') as temp_file:
        temp_file.write(test_data)
        temp_file_path = temp_file.name

    # Отладочная информация
    print(f"Путь к временному файлу: {temp_file_path}")
    with open(temp_file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        print(f"Содержимое файла: {file_content}")

    df = read_csv(temp_file_path)


def test_read_excel():
    test_data = pd.DataFrame({
        "id": [1, 2],
        "name": ["Alice", "Bob"],
        "value": [100, 200]
    })
    with NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_file:
        test_data.to_excel(temp_file.name, index=False)
        temp_file_path = temp_file.name

    df = read_excel(temp_file_path)

    assert isinstance(df, pd.DataFrame)

    pd.testing.assert_frame_equal(df.reset_index(drop=True), test_data)


def test_read_csv_with_invalid_file():
    invalid_file = "non_existent_file.csv"
    df = read_csv(invalid_file)
    assert df is None


def test_read_excel_with_invalid_file():
    invalid_file = "non_existent_file.xlsx"
    df = read_excel(invalid_file)
    assert df is None
