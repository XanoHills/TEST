import sys
from typing import Tuple


def input_mistake(hex_color):
    return (not hex_color.startswith("#") or len(hex_color) != 7
            or not all(c.upper() in "0123456789ABCDEF" for c in hex_color[1:]))


def is_gray(hex_color: str) -> bool:
    # Извлекаем значения составляющих цвета
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    # Проверяем, является ли цвет серым
    return r == g == b


def to_gray(hex_color: str) -> Tuple[int, int, int]:
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    # Вычисляем значения, которые нужно прибавить к каждой составляющей, чтобы сделать цвет серым
    delta_r, delta_g, delta_b = 128 - r, 128 - g, 128 - b

    return delta_r, delta_g, delta_b


print("\nГлавное меню: ")
print("Введите цвет в формате '#HHHHHH', где H - любой символ шестнадцатеричного кода (от 0 до F).")
print("0 - выход из программы")

while True:
    hex_color = input("Введите значение: ")
    hex_color = hex_color.replace(' ', '')

    if hex_color == '0':
        sys.exit("\nВыход из программы")

    if input_mistake(hex_color):
        print("\nНекорректный формат ввода. Пожалуйста, введите цвет в формате '#HHHHHH'.")
        continue

    if not is_gray(hex_color):
        result = to_gray(hex_color)
        print(f"\nДля преобразования цвета {hex_color} в серый добавьте к каждой компоненте {result} в RGB кодировке.")

    else:
        print(f"Цвет {hex_color} является серым.")