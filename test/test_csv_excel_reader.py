import pytest
import pandas as pd
from src.csv_excel_reader import read_csv, read_excel

def test_read_csv():
    # Тестовый CSV-файл
    csv_file = "test_data.csv"
    df = read_csv(csv_file)
    assert isinstance(df, pd.DataFrame)

def test_read_excel():
    # Тестовый Excel-файл
    excel_file = "test_data.xlsx"
    df = read_excel(excel_file)
    assert isinstance(df, pd.DataFrame)