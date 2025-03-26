def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает её маску"""
    new_mask_card = card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]
    return new_mask_card


def get_mask_account(card_number: str) -> str:
    """Функция, которая принимает на вход номер счёта и возвращает его маску"""
    return f"**{card_number[-4:]}"


import logging
import os

os.makedirs('logs', exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def create_mask(mask_length: int) -> str:
    """
    Пример функции в модуле masks с логированием и типизацией.
    """
    logger.debug(f"Вызов create_mask с mask_length={mask_length}")
    if mask_length < 0:
        logger.error("Отрицательная длина маски недопустима")
        raise ValueError("mask_length must be non-negative")
    mask = "*" * mask_length
    logger.info(f"Маска создана: {mask}")
    return mask
