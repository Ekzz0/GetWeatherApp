from .data_structures import Menu, Action

MAIN_MENU_OPTIONS = [
    Menu(number=1,
         action_label="Определить погоду (по координатам)\n",
         action=Action.TEMP_BY_COORDS),
    Menu(number=2,
         action_label="Определить погоду (по городу)\n",
         action=Action.TEMP_BY_CITY_NAME),
    Menu(number=3,
         action_label="Определить погоду (по текущему местоположению)\n",
         action=Action.TEMP_BY_IP),
    Menu(number=4,
         action_label="Посмотреть историю запросов (последние n штук)\n",
         action=Action.VIEW_HISTORY),
    Menu(number=5,
         action_label="Очистить историю запросов\n",
         action=Action.CLEAR_HISTORY),
    Menu(number=6,
         action_label="Завершить работу приложения\n",
         action=Action.END_APP),
]

TEMP_BY_COORDS_OPTIONS = [
    Menu(number=1,
         action_label="Ввести координаты\n",
         action=Action.INPUT_COORDS),
    Menu(number=2,
         action_label="Назад\n",
         action=Action.MAIN_MENU),
    Menu(number=3,
         action_label="Завершить работу приложения\n",
         action=Action.END_APP),
]

TEMP_BY_CITY_NAME_OPTIONS = [
    Menu(number=1,
         action_label="Ввести название города\n",
         action=Action.INPUT_CITY_NAME),
    Menu(number=2,
         action_label="Назад\n",
         action=Action.MAIN_MENU),
    Menu(number=3,
         action_label="Завершить работу приложения\n",
         action=Action.END_APP),
]

BACK_AND_END_OPTIONS = [
    Menu(number=1,
         action_label="Назад\n",
         action=Action.MAIN_MENU),
    Menu(number=2,
         action_label="Завершить работу приложения\n",
         action=Action.END_APP),
]
