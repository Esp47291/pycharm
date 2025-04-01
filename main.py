from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    card_number = 1234567890123456
    account_number = 9876543210123456

    print("Маскированный номер карты:", get_mask_card_number(card_number))
    print("Маскированный номер счета:", get_mask_account(account_number))

from utils.utils import do_something
from masks.masks import create_mask


def main() -> None:
    # Примеры вызова функций, где логируются результаты
    result = do_something(10, 2)
    print("Результат:", result)

    mask = create_mask(5)
    print("Созданная маска:", mask)


if __name__ == "__main__":
    main()
