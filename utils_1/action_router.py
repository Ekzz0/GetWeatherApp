import json
import traceback
from dataclasses import dataclass
from typing import Callable

from utils.errors_processing import requests_errors
from utils.getters import get_city_name_by_coordinates, get_weather, get_location_by_ip, get_coordinates
from utils_1.config import PATH_HISTORY, WeatherInfo, Coordinates, MenuLists, Action, Option
from utils_1.io_scripts import clear_menu, input_count, print_row_from_json, input_coords
from utils_1.json_scripts import read_json, fill_json


class HistoryMethods:
    # Алгоритм действия 'Очистить историю'
    def clear_history(self):
        with open(PATH_HISTORY, 'w'):
            pass

        # Алгоритм действия 'Посмотреть историю'

    def data_from_history(self):
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


class WeatherMethods:
    def __init__(self):
        self.Weather = WeatherInfo()
        self.Coords = Coordinates()

    @requests_errors
    def get_city_name_by_coordinates(self):
        """
        Получение названия города по координатам (lat, lon)
        :return: city_name
        """
        while True:
            self.Coords = input_coords()
            try:
                Weather = get_city_name_by_coordinates(self.Coords)
                clear_menu()
            except (IndexError, KeyError):
                clear_menu()
            else:
                self.Weather = Weather
                return

    # Чики бамбони
    @requests_errors
    def get_weather(self):
        """
        Запрос на OpenWeatherMap API и его обработка
        :param
        :return: WeatherInfo
        """
        self.Weather = get_weather(self.Coords, self.Weather)

    # Чики бамбони
    @requests_errors
    def get_coordinates_by_ip(self):
        """
        Запрос на ipinfo для получения данных по ip адресу и его обработка
        :return: Coordinates, WeatherInfo
        """
        # TODO: Добавить обработку ошибок, связанных с невозможностью получения координат по Ip
        self.Coords, self.Weather = get_location_by_ip()

    @requests_errors
    def get_coordinates_by_city_name(self):
        """
        Получение координат по названию города.
        :return: координаты и название города в WeatherInfo
        """
        while True:
            city_name = input("Введите название города: ").strip()
            try:
                # Получение координат
                Coords = get_coordinates(city_name)
                clear_menu()
            except (IndexError, KeyError):
                # Обработка ошибки, связанной с неверно введенным названием
                clear_menu()
            else:
                self.Coords = Coords
                self.Weather.city_name = city_name
                return

    def end(self):
        fill_json(self.Weather)
        self.Weather.print_weather_info()


class TaskManager:
    def do_tasks(self, tasks, methods):
        for task in tasks:
            clear_menu()
            # try:
            task.func(methods)
            # except Exception as e:
            #     print('Что-то пошло не так. Возможно, по вашим координатам не удалось получить прогноз.')
            #     print(e)
            # else:
            clear_menu()

    # TODO: Возможно этот метод можно заменить namedtuple-ом
    # Маршрутизатор, который возвращает опции для выбранного в интерфейсе меню
    def get_options(self, action: Action = Action.MAIN_MENU) -> Option | None:
        if action == Action.END_APP:
            quit()
        elif action == Action.MAIN_MENU:
            return Option(
                func=None,
                menu_list=MenuLists.MAIN_MENU_OPTIONS
            )
        elif action == Action.TEMP_BY_COORDS:
            return Option(
                func=self.do_tasks,
                args=TaskList.WEATER_BY_COORDS_TASKS,
                methods=WeatherMethods,
                menu_list=MenuLists.BACK_AND_END_OPTIONS
            )
        elif action == Action.TEMP_BY_CITY_NAME:
            return Option(
                func=self.do_tasks,
                args=TaskList.WEATER_BY_CITY_NAME,
                methods=WeatherMethods,
                menu_list=MenuLists.BACK_AND_END_OPTIONS
            )
        elif action == Action.TEMP_BY_IP:
            return Option(
                func=self.do_tasks,
                args=TaskList.WEATER_BY_IP,
                methods=WeatherMethods,
                menu_list=MenuLists.BACK_AND_END_OPTIONS
            )
        elif action == Action.VIEW_HISTORY:
            return Option(
                func=self.do_tasks,
                args=TaskList.VIEW_HISTORY,
                methods=HistoryMethods,
                menu_list=MenuLists.BACK_AND_END_OPTIONS
            )
        elif action == Action.CLEAR_HISTORY:
            return Option(
                head="История очищена!\nГлавное меню:".upper(),
                func=self.do_tasks,
                args=TaskList.CLEAR_HISTORY,
                methods=HistoryMethods,
                menu_list=MenuLists.MAIN_MENU_OPTIONS
            )



@dataclass
class Task:
    func: Callable


@dataclass
class TaskList:
    WEATER_BY_COORDS_TASKS = [
        Task(func=WeatherMethods.get_city_name_by_coordinates),
        Task(func=WeatherMethods.get_weather),
        Task(func=WeatherMethods.end)
    ]
    WEATER_BY_IP = [
        Task(func=WeatherMethods.get_coordinates_by_ip),
        Task(func=WeatherMethods.get_weather),
        Task(func=WeatherMethods.end)
    ]
    WEATER_BY_CITY_NAME = [
        Task(func=WeatherMethods.get_coordinates_by_city_name),
        Task(func=WeatherMethods.get_weather),
        Task(func=WeatherMethods.end)
    ]
    CLEAR_HISTORY = [
        Task(func=HistoryMethods.clear_history)
    ]
    VIEW_HISTORY = [
        Task(func=HistoryMethods.data_from_history)
    ]



