from .action_scripts import by_coords_action, by_city_name_action, by_ip_action, \
    data_from_history, clear_history
from .config import MenuLists, Action, Option


# Маршрутизатор, который возвращает опции для выбранного в интерфейсе меню
def get_options_by_action_name(action: Action = Action.MAIN_MENU) -> Option | None:
    if action == Action.END_APP:
        quit()
    elif action == Action.MAIN_MENU:
        return Option(
            func=None,
            menu_list=MenuLists.MAIN_MENU_OPTIONS
        )
    elif action == Action.TEMP_BY_COORDS:
        return Option(
            func=by_coords_action,
            menu_list=MenuLists.BACK_AND_END_OPTIONS
        )
    elif action == Action.TEMP_BY_CITY_NAME:
        return Option(
            func=by_city_name_action,
            menu_list=MenuLists.BACK_AND_END_OPTIONS
        )
    elif action == Action.TEMP_BY_IP:
        return Option(
            func=by_ip_action,
            menu_list=MenuLists.BACK_AND_END_OPTIONS
        )
    elif action == Action.VIEW_HISTORY:
        return Option(
            func=data_from_history,
            menu_list=MenuLists.BACK_AND_END_OPTIONS
        )
    elif action == Action.CLEAR_HISTORY:
        return Option(
            head="История очищена!\nГлавное меню:".upper(),
            func=clear_history,
            menu_list=MenuLists.MAIN_MENU_OPTIONS
        )
