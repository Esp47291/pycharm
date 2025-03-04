import os
import pytest
from src.decorators import log


# Фикстура для очистки файла логов перед каждым тестом
@pytest.fixture
def clear_log_file():
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")


# Тест для логирования в файл
def test_log_to_file(clear_log_file):
    @log(filename="mylog.txt")
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)

    with open("mylog.txt", "r", encoding="utf-8") as file:
        log_content = file.read()
    assert "add ok" in log_content


# Тест для логирования в консоль
def test_log_to_console(capsys):
    @log()
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(3, 4)

    captured = capsys.readouterr()
    assert isinstance(captured.out, object)
    assert "multiply ok" in captured.out


# Тест для логирования ошибок
def test_log_error(clear_log_file):
    @log(filename="mylog.txt")
    def divide(a: int, b: int) -> float:
        return a / b

    divide(1, 0)  # Деление на ноль вызовет ошибку
    with open("mylog.txt", "r", encoding="utf-8") as file:
        log_content = file.read()
    assert "divide error: ZeroDivisionError" in log_content