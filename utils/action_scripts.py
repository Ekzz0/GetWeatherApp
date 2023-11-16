from .open_weather_api_scripts import coordinates_by_city_name, weather_by_entered_coordinates, coordinates_by_ip, \
    weather_by_received_coordinates
from .json_scripts import fill_json, read_json
from .io_scripts import input_count, print_row_from_json, clear_menu
import traceback
import json
from .config import PATH_HISTORY, WeatherInfo


# Алгоритм действия 'Выбор температуры по текущему местоположению'
def by_ip_action():
    try:
        clear_menu()
        Coords, Weather = coordinates_by_ip()
        Weather = weather_by_received_coordinates(Coords, Weather)
        clear_menu()
        fill_json(Weather)
        Weather.print_weather_info()
    # Учёт конкретных ошибок происходит на более низком уровне
    except Exception as e:
        print("Неизвестная ошибка:", type(e), e)
        print(traceback.format_exc())
        quit()


# Алгоритм действия 'Выбор температуры по городу'
def by_city_name_action():
    try:
        clear_menu()
        Coords, Weather = coordinates_by_city_name()
        Weather = weather_by_received_coordinates(Coords, Weather)
        clear_menu()
        fill_json(Weather)
        Weather.print_weather_info()
    # Учёт конкретных ошибок происходит на более низком уровне
    except Exception as e:
        print("Неизвестная ошибка:", type(e), e)
        print(traceback.format_exc())
        quit()


# Алгоритм действия 'Выбор температуры по координатам'
def by_coords_action():
    try:
        clear_menu()
        Weather = weather_by_entered_coordinates()
        clear_menu()
        fill_json(Weather)
        Weather.print_weather_info()
    # Учёт конкретных ошибок происходит на более низком уровне
    except Exception as e:
        print("Неизвестная ошибка.", type(e), e)
        print(traceback.format_exc())
        quit()


# Алгоритм действия 'Посмотреть историю'
def data_from_history():
    try:
        data = read_json(PATH_HISTORY)
    except json.decoder.JSONDecodeError:
        clear_menu()
        print("Файл пуст.")
    else:
        print("Количество записей в истории:", len(data))
        count = input_count()
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
                for i, row in enumerate(data[::-1][:count]):
                    print_row_from_json(i, row)
        except Exception as e:
            clear_menu()
            print("Неизвестная ошибка:", type(e), e)
            print(traceback.format_exc())


# Алгоритм действия 'Очистить историю'
def clear_history():
    with open(PATH_HISTORY, 'w'):
        pass
