from typing import Tuple

def is_gray(hex_color: str) -> bool:
    # Проверка на корректный формат ввода
    if not hex_color.startswith("#") or len(hex_color) != 7 or not all(c.upper() in "0123456789ABCDEF" for c in hex_color[1:]):
        print("Некорректный формат ввода. Пожалуйста, введите цвет в формате '#HHHHHH'.")
        return False

    # Извлекаем значения цветовых компонент
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    # Проверяем, является ли цвет серым
    return r == g == b

def to_gray(hex_color: str) -> Tuple[int, int, int]:
    # Проверка на корректный формат ввода
    if not hex_color.startswith("#") or len(hex_color) != 7 or not all(c.upper() in "0123456789ABCDEF" for c in hex_color[1:]):
        print("Некорректный формат ввода. Пожалуйста, введите цвет в формате '#HHHHHH'.")
        return (0, 0, 0)

    # Извлекаем значения цветовых компонент
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    # Вычисляем значения, которые нужно прибавить к каждой компоненте, чтобы сделать цвет серым
    delta_r, delta_g, delta_b = 128 - r, 128 - g, 128 - b

    return (delta_r, delta_g, delta_b)

# Меню программы
while True:
    print("\nМеню:")
    print("1. Проверить, является ли цвет серым")
    print("2. Получить значения для преобразования цвета в серый")
    print("3. Выход")

    choice = input("Выберите действие (1, 2, 3): ")

    if choice == "1":
        hex_color = input("Введите цвет в формате '#HHHHHH': ")
        result = is_gray(hex_color)
        print(f"Цвет {hex_color} является серым: {result}")
    elif choice == "2":
        hex_color = input("Введите цвет в формате '#HHHHHH': ")
        result = to_gray(hex_color)
        print(f"Для преобразования цвета {hex_color} в серый добавьте к каждой компоненте: {result}")
    elif choice == "3":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")