from .open_weather_api_scripts import get_report_geo_by_city_name, get_report_weather_by_coords, \
    get_report_weather_by_report_geo, get_report_geo_by_current_geo
from .json_scripts import fill_json, read_json
from .io_scripts import get_count_from_console, print_weather_info, print_row_from_json, clear_menu
from .constants import dict_with_action_options, dict_with_weather_info
# import traceback
import json


def void():
    """
    Метод используется для вызова пустой функции
    """
    pass


def get_options_by_action_name(action: str) -> dict_with_action_options:
    """
    Формат словаря options: {key: {action_head: ..., action: ...}
    - key – это номер действия в меню, по которому происходит переключение на другое меню (или func/head).
    - head – это заголовок выбранного меню.
    - func – это функция, которая должна выполниться при запуске меню.
    - action_head – это заголовок действия, которое отображается в меню с соответствующим ему номером.
    - action – это название следующего меню, к которому осуществится переход после выбора действия.

    :param action: название выбранного действия.
    :return: dict_with_action_options
    """
    # Параметры для действия 'Конец'
    if action == 'Конец':
        quit()
    # Параметры для действия 'Главное меню'
    if action == 'Главное меню':
        options = {'1': {"action_head": "Определить погоду (по координатам)\n",
                         "action": 'Выбор температуры по координатам'},
                   '2': {"action_head": "Определить погоду (по городу)\n",
                         "action": 'Выбор температуры по городу'},
                   '3': {"action_head": "Определить погоду (по текущему местоположению)\n",
                         "action": 'Выбор температуры по текущему местоположению'},
                   '4': {"action_head": "Посмотреть историю запросов (последние n штук)\n",
                         "action": 'Посмотреть историю'},
                   '5': {"action_head": "Очистить историю запросов\n",
                         "action": 'Очистить историю'},
                   '6': {"action_head": "Завершить работу приложения\n",
                         "action": "Конец"},
                   "head": "Главное меню:".upper(),
                   "func": void}
        return options
    # Параметры для действия 'Выбор температуры по координатам'
    elif action == 'Выбор температуры по координатам':
        options = {'1': {"action_head": "Ввести координаты\n",
                         "action": 'Ввести координаты'},
                   '2': {"action_head": "Назад\n",
                         "action": "Главное меню"},
                   '3': {"action_head": "Завершить работу приложения\n",
                         "action": "Конец"},
                   "head": "Определить текущую погоду (по координатам):".upper(),
                   "func": void}
        return options
    # Параметры для действия 'Выбор температуры по городу'
    elif action == 'Выбор температуры по городу':
        options = {'1': {"action_head": "Ввести название города\n",
                         "action": 'Ввести название города'},
                   '2': {"action_head": "Назад\n",
                         "action": "Главное меню"},
                   '3': {"action_head": "Завершить работу приложения\n",
                         "action": "Конец"},
                   "head": "Определить текущую погоду (по городу):".upper(),
                   "func": void}
        return options
    # Параметры для действия 'Ввести координаты'
    elif action == 'Ввести координаты':
        options = {'1': {"action_head": "Назад в главное меню\n",
                         "action": "Главное меню"},
                   '2': {"action_head": "Завершить работу приложения\n",
                         "action": "Конец"},
                   "func": choose_by_coords_action}
        return options
    # Параметры для действия 'Ввести название города'
    elif action == 'Ввести название города':
        options = {'1': {"action_head": "Назад в главное меню\n",
                         "action": "Главное меню"},
                   '2': {"action_head": "Завершить работу приложения\n",
                         "action": "Конец"},
                   "func": choose_by_city_name_action}
        return options
    # Параметры для действия 'Выбор температуры по текущему местоположению'
    elif action == 'Выбор температуры по текущему местоположению':
        options = {'1': {"action_head": "Назад в главное меню\n",
                         "action": "Главное меню"},
                   '2': {"action_head": "Завершить работу приложения\n",
                         "action": "Конец"},
                   "func": choose_by_current_geo_action}
        return options
    # Параметры для действия 'Посмотреть историю'
    elif action == 'Посмотреть историю':
        options = {'1': {"action_head": "Назад в главное меню\n",
                         "action": "Главное меню"},
                   '2': {"action_head": "Завершить работу приложения\n",
                         "action": "Конец"},
                   "func": get_data_to_history}
        return options
    # Параметры для действия 'Очистить историю'
    elif action == 'Очистить историю':
        options = {'1': {"action_head": "Определить погоду (по координатам)\n",
                         "action": 'Выбор температуры по координатам'},
                   '2': {"action_head": "Определить погоду (по городу)\n",
                         "action": 'Выбор температуры по городу'},
                   '3': {"action_head": "Определить погоду (по текущему местоположению)\n",
                         "action": 'Выбор температуры по текущему местоположению'},
                   '4': {"action_head": "Посмотреть историю запросов (последние n штук)\n",
                         "action": 'Посмотреть историю'},
                   '5': {"action_head": "Очистить историю запросов\n",
                         "action": 'Очистить историю'},
                   '6': {"action_head": "Завершить работу приложения\n",
                         "action": "Конец"},
                   "head": "История очищена!\nГлавное меню:".upper(),
                   "func": clear_history}
        return options


def choose_by_current_geo_action():
    """
    Алгоритм действия 'Выбор температуры по текущему местоположению'
    """
    try:
        clear_menu()
        report_geo = get_report_geo_by_current_geo()
        report_weather = get_report_weather_by_report_geo(report_geo)
        clear_menu()
        add_data_to_history(report_weather)
        print_weather_info(report_weather)
    # Учёт конкретных ошибок происходит на более низком уровне
    except Exception as e:
        print("Неизвестная ошибка:", type(e), e)
        # print(traceback.format_exc())
        quit()


def choose_by_city_name_action():
    """
    Алгоритм действия 'Выбор температуры по городу'
    """
    try:
        clear_menu()
        report_geo = get_report_geo_by_city_name()
        report_weather = get_report_weather_by_report_geo(report_geo)
        clear_menu()
        add_data_to_history(report_weather)
        print_weather_info(report_weather)
    # Учёт конкретных ошибок происходит на более низком уровне
    except Exception as e:
        print("Неизвестная ошибка:", type(e), e)
        # print(traceback.format_exc())
        quit()


def choose_by_coords_action():
    """
    Алгоритм действия 'Выбор температуры по координатам'
    """
    try:
        clear_menu()
        report_weather = get_report_weather_by_coords()
        clear_menu()
        add_data_to_history(report_weather)
        print_weather_info(report_weather)

    # Учёт конкретных ошибок происходит на более низком уровне
    except Exception as e:
        print("Неизвестная ошибка.", type(e), e)
        # print(traceback.format_exc())
        quit()


def add_data_to_history(data: dict_with_weather_info):
    fill_json(data)


def get_data_to_history():
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
            # print(traceback.format_exc())


def clear_history():
    """
    Алгоритм действия 'Очистить историю'
    """
    with open("history/history.json", 'w'):
        pass
