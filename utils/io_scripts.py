import os
from .constants import dict_with_weather_info
from .data_structures import Coordinates, WeatherInfo
from dacite import from_dict


def clear_menu():
    """
    # Очищение консоли
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_row_from_json(i: int, row: dict_with_weather_info):
    """
    Метод для вывода данных из json файла в консоль.
    :param i: номер индекса в словаре.
    :param row: словарь с данными
    """
    print(f"Запрос номер {i + 1}:")
    Weather = from_dict(data_class=WeatherInfo, data=row)
    Weather.print_weather_info()
    print()


def get_count_from_console() -> int:
    """
    Метод для получения числа записей, которых пользователь желает просмотреть.
    :return: count число записей
    """
    while True:
        try:
            # Получение координат
            count = int(input("Введите количество записей для просмотра: ").strip())
        except ValueError:
            # Обработка ошибки, связанной с неверно введёнными координатами
            clear_menu()
            print("Введите число еще раз, пожалуйста\n")
        else:
            # Возвращение верно введённых координат
            return count


def get_coords_by_console() -> Coordinates:
    """
    Получение координат (lat, lon) из консоли
    :return: (lat, lon)
    """
    while True:
        try:
            # Получение координат
            lat, lon = map(float, input("Введите два числа, разделяя их запятой и пробелом (a, b)\n"
                                        "Координаты: ").strip().split(', '))
        except ValueError:
            # Обработка ошибки, связанной с неверно введёнными координатами
            clear_menu()
            print("Вы неверно ввели координаты. Попробуйте еще раз\n")
        else:
            # Возвращение верно введённых координат
            return Coordinates(lat=lat, lon=lon)
