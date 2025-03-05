import os
import pytest
from src.decorators import log

@pytest.fixture
def clear_log_file():
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")

def test_log_to_file(clear_log_file):
    @log(filename="mylog.txt")
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)

    with open("mylog.txt", "r", encoding="utf-8") as file:
        log_content = file.read()
    assert "add ok" in log_content

def test_log_to_console(capsys):
    @log()
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(3, 4)
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out

def test_log_error(clear_log_file):
    @log(filename="mylog.txt")
    def divide(a: int, b: int) -> float:
        return a / b

    # Деление на ноль вызовет ошибку
    divide(1, 0)

    with open("mylog.txt", "r", encoding="utf-8") as file:
        log_content = file.read()
    assert "divide error: ZeroDivisionError" in log_content