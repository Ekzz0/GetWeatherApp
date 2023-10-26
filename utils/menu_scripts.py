import subprocess
# from .actions_scripts import select_options_by_action_name
from .requests_scripts import weather_map_get, geocoding_get


def print_weather_info(report: dict[str, float]):
    """
    Метод, который выводит данные о погоде.
    :param report: Словарь с данными о текущей погоде
    """
    print('Название города:', report.get("city_name", "Город не указан"))
    print('Погодные условия:', report['weather_description'])
    print('Текущая температура:', report['current_temp'], 'градусов по цельсию')
    print('Ощущается как:', report['current_temp_feels_like'], 'градусов по цельсию')
    print('Скорость ветра:', report['wind_speed'], 'м/с')


def print_options(options: dict[str, tuple, None]):
    """
    Метод, который печатает в консоль данные возможных действий.
    :param options: - словарь с возможными действиями и их номерами
    """
    print()

    # Try-except использован для того, чтобы выводить в консоль только те элементы словаря options,
    # которые имею ключ - целое число, т.к. в словаре хранятся и значения с ключами другого формата
    try:
        for key, value in options.items():
            print(f'{int(key)}: {value[0]}', end='')
    except:
        pass
    print()


def show_menu(options: dict[str, tuple, None]):
    """
    Отображение меню по указанным возможным действиям и заголовку. При необходимости
    выполняет переданную функцию.
    :param options:
    """
    # Очистка консоли и отображение заголовка
    clear_menu()
    print(options['head'])

    # Вызов функции, если необходимо
    if options['func_and_args']:
        func = options['func_and_args']
        func()

    # Вывод в консоль доступных действий
    print_options(options)

    # Выбор следующего действия (меню)
    select_mode(options)


def input_coords_menu() -> tuple:
    try:
        # Получение координат
        lat, lon = map(float, input("Введите два числа, разделяя их запятой и пробелом (a, b)\n"
                                    "Координаты: ").split(', '))
    except:
        # Обработка ошибки, связанной с неверно введёнными координатами
        clear_menu()
        print("!!! Вы неверно ввели координаты. Попробуйте еще раз !!!\n")
        lat, lon = input_coords_menu()

        # Возвращение верно введённых координат
        return lat, lon
    else:
        # Возвращение верно введённых координат
        return lat, lon


def get_report_geo_by_city_name() -> dict[str, float]:
    city_name = input("Введите название города: ").strip()
    try:
        # Получение координат
        report_geo = geocoding_get(city_name)
    except:
        # Обработка ошибки, связанной с неверно введенным названием
        clear_menu()
        print("!!! Вы неверно ввели название города. Попробуйте еще раз !!!\n")
        report_geo = get_report_geo_by_city_name()
        return report_geo
    else:
        return report_geo


def select_mode(options: dict[str, tuple, None]):
    try:
        # Выбор действия
        mode = int(input("Выберите действие (введите цифру): "))
        action = options[f'{mode}'][1]
    except:
        # Обработка ошибки, связанной с неверно выбранным меню
        clear_menu()
        show_menu(options)
    else:
        # Получение параметров выбранного меню
        options = get_options_by_action_name(action)

        # Отображение выбранного меню
        show_menu(options)


def clear_menu():
    # Очищение консоли
    subprocess.call('cls', shell=True)


def input_city_name_action():
    subprocess.call('cls', shell=True)
    report_geo = get_report_geo_by_city_name()
    report_weather = weather_map_get(report_geo)
    print_weather_info(report_weather)


def input_coords_action():
    subprocess.call('cls', shell=True)
    lat, lon = input_coords_menu()
    report_geo = {'lat': lat, 'lon': lon}
    report_weather = weather_map_get(report_geo)
    subprocess.call('cls', shell=True)
    print_weather_info(report_weather)


def get_options_by_action_name(action: str) -> dict[str, tuple, None]:
    # Формат словаря options:
    # {key: (head, action_name)
    # key - это номер действия в меню, по которому происходит переключение на другое меню
    # head - это название действия, которое отображается в меню с соответствующим ему номером
    # action_name - это название следующего меню, к которому осуществится переход после выбора действия

    # Параметры для действия 'Конец'
    if action == 'Конец':
        quit()
    # Параметры для действия 'Главное меню'
    if action == 'Главное меню':
        options = {'1': ("Определить текущую погоду (по координатам)\n", 'Выбор температуры по координатам'),
                   '2': ("Определить текущую погоду (по городу)\n", 'Выбор температуры по городу'),
                   '3': ("Посмотреть историю запросов (последние n штук)\n",),
                   '4': ("Очистить историю запросов\n",),
                   '5': ("Завершить работу приложения\n", "Конец"),
                   "head": "Главное меню:",
                   "func_and_args": None}
        return options
    # Параметры для действия 'Выбор температуры по координатам'
    elif action == 'Выбор температуры по координатам':
        options = {'1': ("Ввести координаты\n", 'Ввести координаты'),
                   '2': ("Назад\n", "Главное меню"),
                   '3': ("Завершить работу приложения\n", "Конец"),
                   "head": "Определить текущую погоду (по координатам):",
                   "func_and_args": None}
        return options
    # Параметры для действия 'Выбор температуры по городу'
    elif action == 'Выбор температуры по городу':
        options = {'1': ("Ввести название города\n", 'Ввести название города'),
                   '2': ("Назад\n", "Главное меню"),
                   '3': ("Завершить работу приложения\n", "Конец"),
                   "head": "Определить текущую погоду (по городу):",
                   "func_and_args": None}
        return options
    # Параметры для действия 'Ввести координаты'
    elif action == 'Ввести координаты':
        options = {'1': ("Назад в главное меню\n", "Главное меню"),
                   '2': ("Завершить работу приложения\n", "Конец"),
                   "head": "Прогноз погоды по координатам:\n",
                   "func_and_args": input_coords_action}
        return options
    # Параметры для действия 'Ввести название города'
    elif action == 'Ввести название города':

        # clear_menu()

        options = {'1': ("Назад в главное меню\n", "Главное меню"),
                   '2': ("Завершить работу приложения\n", "Конец"),
                   "head": "Прогноз погоды по координатам:\n",
                   "func_and_args": input_city_name_action}
        return options
    # else:
    #     main_message = "Прогноз погоды по координатам:\n"
    #     options = {"1": ("Назад в главное меню\n", "Главное меню"),
    #                "2": ("Завершить работу приложения\n", "Конец")
    #                }
    #     return options, main_message, None
