
from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    card_number = 1234567890123456
    account_number = 9876543210123456

    print("Маскированный номер карты:", get_mask_card_number(card_number))
    print("Маскированный номер счета:", get_mask_account(account_number))
