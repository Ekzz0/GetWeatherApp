from .action_scripts import by_coords_action, by_city_name_action, by_ip_action, \
    get_data_from_history, clear_history
from .data_structures import Action, Option
from .config import MAIN_MENU_OPTIONS, TEMP_BY_COORDS_OPTIONS, TEMP_BY_CITY_NAME_OPTIONS, BACK_AND_END_OPTIONS


# class ActionRouter:
#     def __init__(self):
#         self.__action = Action.MAIN_MENU
#
#     @property
#     def action_name(self):
#         return self.__action
#
#     @action_name.setter
#     def action_name(self, action_name):
#         self.__action = action_name
#
#     def get_options_by_action(self):
#         pass


def get_options_by_action_name(action: Action = Action.MAIN_MENU) -> Option:
    if action == Action.END_APP:
        quit()
    elif action == Action.MAIN_MENU:
        return Option(
            head="Определить погоду (по координатам)\n".upper(),
            func=None,
            menu_list=MAIN_MENU_OPTIONS
        )
    elif action == Action.TEMP_BY_COORDS:
        return Option(
            head="Определить текущую погоду (по координатам):\n".upper(),
            func=None,
            menu_list=TEMP_BY_COORDS_OPTIONS
        )
    elif action == Action.TEMP_BY_CITY_NAME:
        return Option(
            head="Определить текущую погоду (по городу):".upper(),
            func=None,
            menu_list=TEMP_BY_CITY_NAME_OPTIONS
        )
    elif action == Action.INPUT_COORDS:
        return Option(
            func=by_coords_action,
            menu_list=BACK_AND_END_OPTIONS
        )
    elif action == Action.INPUT_CITY_NAME:
        return Option(
            func=by_city_name_action,
            menu_list=BACK_AND_END_OPTIONS
        )
    elif action == Action.TEMP_BY_IP:
        return Option(
            func=by_ip_action,
            menu_list=BACK_AND_END_OPTIONS
        )
    elif action == Action.VIEW_HISTORY:
        return Option(
            func=get_data_from_history,
            menu_list=BACK_AND_END_OPTIONS
        )
    elif action == Action.CLEAR_HISTORY:
        return Option(
            head="История очищена!\nГлавное меню:".upper(),
            func=clear_history,
            menu_list=MAIN_MENU_OPTIONS
        )
