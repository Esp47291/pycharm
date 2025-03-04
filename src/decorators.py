from typing import Callable, Any, Optional
import datetime


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    :param filename: Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    :return: Декорированная функция.
    """

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Формируем сообщение для логирования
            log_message: str = f"{datetime.datetime.now()} - {func.name}"

            try:
                result: object = func(*args, **kwargs)
                log_message += f" ok\n"
            except Exception as e:
                log_message += f" error: {type(e).name}. Inputs: {args}, {kwargs}\n"
                result = None

            # Логирование в файл или консоль
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message, end="")

            return result
        return wrapper

    return decorator