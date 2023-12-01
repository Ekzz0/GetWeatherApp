# TODO: Автоматизировать инициализацию маршрутов
# Маршрутизатор, который возвращает опции для выбранного в интерфейсе меню

from utils.config import Action, Option, TaskList, MenuLists, TaskName
from .action_methods import get_city_name_by_coordinates, get_weather, end, get_coordinates_by_ip, \
    get_coordinates_by_city_name, void, close
from types import MappingProxyType

from .history_scripts import data_from_history, clear_history


class Router:
    def __init__(self):
        self.dictionary = {}

    def register_function(self, action, option):
        self.dictionary[action] = option

    def select(self, action=Action.MAIN_MENU):
        return self.dictionary.get(action)


# Создадим экземпляр роутера для опций
options_router = Router()
options_router.register_function(Action.END_APP, Option(args=TaskList.CLOSE_APP, menu_list=[]))
options_router.register_function(Action.MAIN_MENU, Option(args=TaskList.PASS, menu_list=MenuLists.MAIN_MENU_OPTIONS))
options_router.register_function(Action.TEMP_BY_COORDS, Option(args=TaskList.WEATER_BY_COORDS_TASKS,
                                                               menu_list=MenuLists.BACK_AND_END_OPTIONS))
options_router.register_function(Action.TEMP_BY_CITY_NAME, Option(args=TaskList.WEATER_BY_CITY_NAME,
                                                                  menu_list=MenuLists.BACK_AND_END_OPTIONS))
options_router.register_function(Action.TEMP_BY_IP, Option(args=TaskList.WEATER_BY_IP,
                                                           menu_list=MenuLists.BACK_AND_END_OPTIONS))
options_router.register_function(Action.VIEW_HISTORY, Option(args=TaskList.VIEW_HISTORY,
                                                             menu_list=MenuLists.BACK_AND_END_OPTIONS))
options_router.register_function(Action.CLEAR_HISTORY, Option(head="История очищена!\nГлавное меню:".upper(),
                                                              args=TaskList.CLEAR_HISTORY,
                                                              menu_list=MenuLists.MAIN_MENU_OPTIONS))
options_router.dictionary = MappingProxyType(options_router.dictionary)


# Создадим экземпляр роутера для функций
functions_router = Router()
functions_router.register_function(TaskName.PASS, void)
functions_router.register_function(TaskName.END, end)
functions_router.register_function(TaskName.GET_WEATHER, get_weather)
functions_router.register_function(TaskName.CITY_BY_COORDS, get_city_name_by_coordinates)
functions_router.register_function(TaskName.COORDS_BY_IP, get_coordinates_by_ip)
functions_router.register_function(TaskName.COORDS_BY_CITY, get_coordinates_by_city_name)
functions_router.register_function(TaskName.VIEW_HISTORY, data_from_history)
functions_router.register_function(TaskName.CLEAR_HISTORY, clear_history)
functions_router.register_function(TaskName.CLOSE_APP, close)
functions_router.dictionary = MappingProxyType(functions_router.dictionary)


