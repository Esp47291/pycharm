# My Bank Operations Project
## Описание проекта
#### Проект предназначен для работы с банковскими операциями. В частности, содержит функции для:
#### фильтрации операций по статусу (filter_by_state),
#### сортировки операций по дате (sort_by_date).

### Проект написан на Python и придерживается GitFlow для ведения разработки.
#### Установка
Склонируйте репозиторий:
git clone https://github.com/username/my_bank_operations_project.git

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

## Тестирование pytest: 

было проведено тестирование каждой функции

# Модуль `generators`

Модуль содержит функции для работы с транзакциями:

1. **`filter_by_currency`**:
   - Фильтрует транзакции по заданной валюте.
   - Пример использования:
     ```python
     usd_transactions = filter_by_currency(transactions, "USD")
     for transaction in usd_transactions:
         print(transaction)
     ```

2. **`transaction_descriptions`**:
   - Возвращает описания транзакций.
   - Пример использования:
     ```python
     descriptions = transaction_descriptions(transactions)
     for description in descriptions:
         print(description)
     ```

3. **`card_number_generator`**:
   - Генерирует номера банковских карт в заданном диапазоне.
   - Пример использования:
     ```python
     for card_number in card_number_generator(1, 5):
         print(card_number)
     ```
# Модуль `decorators`

Модуль содержит декоратор для логирования вызовов функций.

## Декоратор `log`

Декоратор `log` логирует вызовы функций, включая:
- Время вызова.
- Имя функции.
- Результат выполнения (успех или ошибка).
- Входные параметры (в случае ошибки).

### Параметры:
- `filename` (опционально): Имя файла для записи логов. Если не указано, логи выводятся в консоль.

### Пример использования:

```python
from decorators import log

@log(filename="mylog.txt")
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)