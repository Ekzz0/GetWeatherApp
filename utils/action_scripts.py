from .open_weather_api_scripts import get_coordinates_by_city_name, get_weather_by_coordinates, get_coordinates_by_ip, \
    get_weather_by_location
from .json_scripts import fill_json, read_json
from .io_scripts import get_count_from_console, print_row_from_json, clear_menu
import traceback
import json
from .data_structures import WeatherInfo


def by_current_geo_action():
    """
    Алгоритм действия 'Выбор температуры по текущему местоположению'
    """
    try:
        clear_menu()
        Coords, Weather = get_coordinates_by_ip()
        Weather = get_weather_by_location(Coords, Weather)
        clear_menu()
        add_data_to_history(Weather)
        Weather.print_weather_info()
    # Учёт конкретных ошибок происходит на более низком уровне
    except Exception as e:
        print("Неизвестная ошибка:", type(e), e)
        print(traceback.format_exc())
        quit()


def by_city_name_action():
    """
    Алгоритм действия 'Выбор температуры по городу'
    """
    try:
        clear_menu()
        Coords, Weather = get_coordinates_by_city_name()
        Weather = get_weather_by_location(Coords, Weather)
        clear_menu()
        add_data_to_history(Weather)
        Weather.print_weather_info()
    # Учёт конкретных ошибок происходит на более низком уровне
    except Exception as e:
        print("Неизвестная ошибка:", type(e), e)
        print(traceback.format_exc())
        quit()


def by_coords_action():
    """
    Алгоритм действия 'Выбор температуры по координатам'
    """
    try:
        clear_menu()
        Weather = get_weather_by_coordinates()
        clear_menu()
        add_data_to_history(Weather)
        Weather.print_weather_info()

    # Учёт конкретных ошибок происходит на более низком уровне
    except Exception as e:
        print("Неизвестная ошибка.", type(e), e)
        print(traceback.format_exc())
        quit()


def add_data_to_history(data: WeatherInfo):
    fill_json(data)


def get_data_from_history():
    """
    Алгоритм действия 'Посмотреть историю'
    """
    try:
        data = read_json("history/history.json")
    except json.decoder.JSONDecodeError:
        clear_menu()
        print("Файл пуст.")
    else:
        print("Количество записей в истории:", len(data))
        count = get_count_from_console()
        clear_menu()
        try:
            if count > len(data):
                clear_menu()
                print(f"Количество записей истории: {len(data)}, что меньше, чем вы хотите получить ({count})."
                      f"\nВывод всех имеющихся:\n")
                # Добавить вывод всех имеющихся
                for i, row in enumerate(data[::-1]):
                    print_row_from_json(i, row)
            else:
                clear_menu()
                # map(print_row_from_json, data[::-1][:count])
                for i, row in enumerate(data[::-1][:count]):
                    print_row_from_json(i, row)
        except Exception as e:
            clear_menu()
            print("Неизвестная ошибка:", type(e), e)
            print(traceback.format_exc())


def clear_history():
    """
    Алгоритм действия 'Очистить историю'
    """
    with open("history/history.json", 'w'):
        pass
