from typing import Callable, Any, Optional
import datetime
from functools import wraps  # Добавьте эту строку для сохранения метаданных


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции. Записывает время вызова,
    имя функции, статус выполнения (успех/ошибка) и входные параметры в файл или stdout.

    Args:
        filename (str, optional): Путь к файлу для записи логов. Если не указано,
            логи выводятся в стандартный поток вывода (print). По умолчанию None.

    Returns:
        Callable: Внешняя обёртка для декорирования функций.

    Пример использования:
        @log("my_log.txt")
        def my_function(x, y):
            return x + y

        my_function(2, 3)  # Лог будет записан в "my_log.txt"

    Формат лога:
        "[Время] - [имя_функции] [ok|error: описание ошибки]. Inputs: args, kwargs"
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)  # Сохраняем имя и docstring исходной функции
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message = f"{datetime.datetime.now()} - {func.__name__}"

            try:
                result = func(*args, **kwargs)
                log_message += " ok"
            except Exception as e:
                log_message += f" error: {type(e).__name__}"
                result = None

            # Добавляем входные параметры только при ошибке
            if "error" in log_message:
                log_message += f". Inputs: {args}, {kwargs}"

            log_message += "\n"

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message, end="")

            return result

        return wrapper

    return decorator
