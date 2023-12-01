import json
import traceback

from .config import PATH_HISTORY, WeatherInfo, Coordinates, MenuLists, Action, Option, TaskList, TaskName
from .io_scripts import clear_menu, input_count, print_row_from_json
from .json_scripts import read_json

from .action_methods import get_city_name_by_coordinates, get_weather, end, get_coordinates_by_ip, \
    get_coordinates_by_city_name, void


# Алгоритм действия 'Очистить историю'
def clear_history(*args, **kwargs):
    with open(PATH_HISTORY, 'w'):
        pass


# Алгоритм действия 'Посмотреть историю'
def data_from_history(*args, **kwargs):
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


class TaskManager:
    def __init__(self):
        self.Weather = WeatherInfo()
        self.Coords = Coordinates()
        self.func = None

    def do_tasks(self, tasks):
        for task in tasks:
            self.select_func(task.func_name)
            clear_menu()
            try:
                self.func(self)
            except Exception as e:
                clear_menu()
                print('Что-то пошло не так.')
            else:
                clear_menu()

    # TODO: Возможно этот метод можно заменить namedtuple-ом
    # Маршрутизатор, который возвращает опции для выбранного в интерфейсе меню
    @staticmethod
    def get_options(action: Action = Action.MAIN_MENU) -> Option | None:
        if action == Action.END_APP:
            quit()
        elif action == Action.MAIN_MENU:
            return Option(
                args=TaskList.PASS,
                menu_list=MenuLists.MAIN_MENU_OPTIONS
            )
        elif action == Action.TEMP_BY_COORDS:
            return Option(
                args=TaskList.WEATER_BY_COORDS_TASKS,
                menu_list=MenuLists.BACK_AND_END_OPTIONS
            )
        elif action == Action.TEMP_BY_CITY_NAME:
            return Option(
                args=TaskList.WEATER_BY_CITY_NAME,
                menu_list=MenuLists.BACK_AND_END_OPTIONS
            )
        elif action == Action.TEMP_BY_IP:
            return Option(
                args=TaskList.WEATER_BY_IP,
                menu_list=MenuLists.BACK_AND_END_OPTIONS
            )
        elif action == Action.VIEW_HISTORY:
            return Option(
                args=TaskList.VIEW_HISTORY,
                menu_list=MenuLists.BACK_AND_END_OPTIONS
            )
        elif action == Action.CLEAR_HISTORY:
            return Option(
                head="История очищена!\nГлавное меню:".upper(),
                args=TaskList.CLEAR_HISTORY,
                menu_list=MenuLists.MAIN_MENU_OPTIONS
            )

    def select_func(self, func_name):
        if func_name == TaskName.PASS:
            self.func = void
        if func_name == TaskName.END:
            self.func = end
        if func_name == TaskName.GET_WEATHER:
            self.func = get_weather
        if func_name == TaskName.CITY_BY_COORDS:
            self.func = get_city_name_by_coordinates
        if func_name == TaskName.COORDS_BY_IP:
            self.func = get_coordinates_by_ip
        if func_name == TaskName.COORDS_BY_CITY:
            self.func = get_coordinates_by_city_name
        if func_name == TaskName.VIEW_HISTORY:
            self.func = data_from_history
        if func_name == TaskName.CLEAR_HISTORY:
            self.func = clear_history

