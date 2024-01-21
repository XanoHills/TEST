import sys
from typing import Tuple


def input_mistake(hex_color):
    """
    Проверяет, является ли введенный шестнадцатеричный код цвета допустимым.

    Args:
        hex_color (str): Введенный шестнадцатеричный код цвета.

    Returns:
        bool: True, если ввод допустим, False в противном случае.

    Examples:
        >>> input_mistake("#1a2b3c")
        False
        >>> input_mistake("1a2b3c")
        True
    """
    return (not hex_color.startswith("#") or len(hex_color) != 7
            or not all(c.upper() in "0123456789ABCDEF" for c in hex_color[1:]))


def is_gray(hex_color: str) -> bool:
    """
    Проверяет, является ли заданный цвет оттенком серого.

    Эта функция извлекает значения красного (r), зеленого (g) и синего (b)
    компонентов из шестнадцатеричного цветового кода.
    Затем она определяет, является ли цвет оттенком серого, проверяя, равны
    ли все три компонента.

    Args:
        hex_color (str): Шестнадцатеричный цветовой код.

    Returns:
        bool: True, если цвет является оттенком серого, False в противном случае.

    Examples:
        >>> is_gray("#808080")
        True
        >>> is_gray("#336699")
        False
    """
    # Извлекаем значения составляющих цвета
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    # Проверяем, является ли цвет серым
    return r == g == b


def to_gray(hex_color: str) -> Tuple[int, int, int]:
    """
    Преобразует цвет в оттенок серого, вычисляя дельты для каждой компоненты RGB.

    Эта функция извлекает значения красного (r), зеленого (g) и синего (b)
    компонентов из шестнадцатеричного цветового кода.
    Затем она вычисляет дельты, необходимые для преобразования цвета в
    оттенок серого, вычитая каждую компоненту из 128.

    Args:
        hex_color (str): Шестнадцатеричный цветовой код.

    Returns:
        Tuple[int, int, int]: Дельты (delta_r, delta_g, delta_b),
        которые нужно добавить к каждой компоненте RGB.

    Examples:
        >>> to_gray("#336699")
        (44, 67, 91)
        >>> to_gray("#AABBCC")
        (-19, -18, -19)
    """
    # Извлекаем значения составляющих цвета
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    # Вычисляем значения, которые нужно прибавить к каждой составляющей,
    # чтобы сделать цвет серым
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
        