import random as ra
from datetime import datetime as dt


def generate_barcode():
    # Тип марки (3 символа)
    mark_type = "".join(ra.choice("0123ABCD") for _ in range(3))

    # Проверка типа марки
    if len(mark_type) != 3:
        raise ValueError("Тип марки должен быть длиной 3 символа")
    if not all(char in "0123ABCD" for char in mark_type):
        raise ValueError(
            "Тип марки должен состоять только из символов 0, 1, 2, 3, A, B, C, D"
        )

    # Серия марки (3 символа)
    mark_series = "".join(ra.choice("0123ABCD") for _ in range(3))

    # Проверка серии марки
    if len(mark_series) != 3:
        raise ValueError("Серия марки должна быть длиной 3 символа")
    if not all(char in "0123ABCD" for char in mark_series):
        raise ValueError(
            "Серия марки должна состоять только из символов 0, 1, 2, 3, A, B, C, D"
        )

    # Номер марки (8 символов)
    mark_number = "".join(ra.choice("0123456789") for _ in range(8))

    # Проверка номера марки
    if len(mark_number) != 8:
        raise ValueError("Номер марки должен быть длиной 8 символов")
    if not all(char in "0123456789" for char in mark_number):
        raise ValueError("Номер марки должен состоять только из цифр")

    # Служебная информация ЕГАИС (7 символов)
    egaiss_info = "".join(ra.choice("0123456789") for _ in range(7))

    # Проверка служебной информации ЕГАИС
    if len(egaiss_info) != 7:
        raise ValueError("Служебная информация ЕГАИС должна быть длиной 7 символов")
    if not all(char in "0123456789" for char in egaiss_info):
        raise ValueError("Служебная информация ЕГАИС должна состоять только из цифр")

    # Контрольная сумма и электронная подпись, созданная при помощи СКЗИ по ГОСТ (129 символов)
    signature = "".join(
        ra.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(129)
    )

    # Проверка контрольной суммы и электронной подписи
    if len(signature) != 129:
        raise ValueError(
            "Контрольная сумма и электронная подпись должны быть длиной 129 символов"
        )
    if not all(char in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" for char in signature):
        raise ValueError(
            "Контрольная сумма и электронная подпись должны состоять только из цифр и заглавных букв"
        )

    # Сборка баркода
    barcode = mark_type + mark_series + mark_number + egaiss_info + signature

    # Проверка длины баркода
    if len(barcode) != 150:
        raise ValueError("Баркод должен быть длиной 150 символов")

    return barcode


# Генерация баркода
try:
    barcode = generate_barcode()
    print(barcode)
except ValueError as e:
    print(f"Error: {e}")
