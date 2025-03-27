import pytest
from unittest.mock import patch
from src.csv_excel_reader import read_transactions_csv, read_transactions_excel

# Тест для CSV
@patch("pandas.read_csv")
def test_read_transactions_csv(mock_read_csv):
    mock_data = pd.DataFrame({
        "id": [1, 2],
        "amount": [100, 200],
        "description": ["Salary", "Rent"]
    })
    mock_read_csv.return_value = mock_data

    result = read_transactions_csv("dummy.csv")
    assert result == [
        {"id": 1, "amount": 100, "description": "Salary"},
        {"id": 2, "amount": 200, "description": "Rent"}
    ]

# Тест для Excel
@patch("pandas.read_excel")
def test_read_transactions_excel(mock_read_excel):
    mock_data = pd.DataFrame({
        "id": [1, 2],
        "amount": [150, 250],
        "description": ["Bonus", "Utilities"]
    })
    mock_read_excel.return_value = mock_data

    result = read_transactions_excel("dummy.xlsx")
    assert result == [
        {"id": 1, "amount": 150, "description": "Bonus"},
        {"id": 2, "amount": 250, "description": "Utilities"}
    ]