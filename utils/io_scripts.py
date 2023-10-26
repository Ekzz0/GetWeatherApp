import datetime
import os
from .constants import dict_with_weather_info


def clear_menu():
    """
    # Очищение консоли
    """
    # pyautogui.hotkey('ctrl', 'l')
    os.system('cls' if os.name == 'nt' else 'clear')


def print_row_from_json(i: int, row: dict_with_weather_info):
    """
    Метод для вывода данных из json файла в консоль.
    :param i: номер индекса в словаре.
    :param row: словарь с данными
    """
    print(f"Запрос номер {i + 1}:")
    print_weather_info(row)
    print()


def print_weather_info(report: dict_with_weather_info):
    """
    Метод, который выводит данные о погоде.
    :param report: Словарь с данными о текущей погоде
    """
    print('Текущее время:', (report['dt']))
    print('Название города:', report["city_name"])
    print('Погодные условия:', report['weather_description'])
    print('Текущая температура:', report['current_temp'], 'градусов по цельсию')
    print('Ощущается как:', report['current_temp_feels_like'], 'градусов по цельсию')
    print('Скорость ветра:', report['wind_speed'], 'м/с')


def get_count_from_console() -> int:
    """
    Метод для получения числа записей, которых пользователь желает просмотреть.
    :return: count число записей
    """
    try:
        # Получение координат
        count = int(input("Введите количество записей для просмотра: ").strip())
    except ValueError:
        # Обработка ошибки, связанной с неверно введёнными координатами
        clear_menu()
        print("Введите число еще раз, пожалуйста\n")
        count = get_count_from_console()

        # Возвращение верно введённых координат
        return count
    else:
        # Возвращение верно введённых координат
        return count


def get_coords_by_console() -> tuple[float, float]:
    """
    Получение координат (lat, lon) из консоли
    :return: (lat, lon)
    """
    try:
        # Получение координат
        lat, lon = map(float, input("Введите два числа, разделяя их запятой и пробелом (a, b)\n"
                                    "Координаты: ").strip().split(', '))
    except ValueError:
        # Обработка ошибки, связанной с неверно введёнными координатами
        clear_menu()
        print("Вы неверно ввели координаты. Попробуйте еще раз\n")
        lat, lon = get_coords_by_console()

        # Возвращение верно введённых координат
        return lat, lon
    else:
        # Возвращение верно введённых координат
        return lat, lon
