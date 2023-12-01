from enum import StrEnum
from dataclasses import dataclass, asdict
from typing import Optional, Callable

# Путь к истории запросов
PATH_HISTORY = "history/history.json"

# Константы для подключения к API
API_KEY = 'd0b91a8a366a27778b9e5c42c592baae'


# Класс для хранения URL адресов
class URLs(StrEnum):
    ULR_GEOCODING_API = 'http://api.openweathermap.org/geo/1.0/direct'
    ULR_GEOCODING_REVERSE_API = "http://api.openweathermap.org/geo/1.0/reverse"
    ULR_WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather'
    URL_IPINFO = 'https://ipinfo.io'


# Класс для хранения названий возможных действий
class Action(StrEnum):
    END_APP = 'Конец'
    MAIN_MENU = 'Главное меню'
    TEMP_BY_COORDS = 'Выбор температуры по координатам'
    TEMP_BY_CITY_NAME = 'Выбор температуры по городу'
    TEMP_BY_IP = 'Выбор температуры по текущему местоположению'
    VIEW_HISTORY = 'Посмотреть историю'
    CLEAR_HISTORY = 'Очистить историю'


# Текстовая информация каждого меню
@dataclass
class Menu:
    number: int
    action_label: str
    action: Action


# Опции для различных меню
@dataclass
class MenuLists:
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
             action=Action.END_APP)
    ]
    BACK_AND_END_OPTIONS = [
        Menu(number=1,
             action_label="Назад\n",
             action=Action.MAIN_MENU),
        Menu(number=2,
             action_label="Завершить работу приложения\n",
             action=Action.END_APP)
    ]


# Опции каждого меню (заголовок, список меню, выполняемая функция)
@dataclass
class Option:
    menu_list: list[Menu]
    head: str = ''
    args: list = None


# Класс данных, имеющие метод dict. От него наследуются другие классы данных, хранящие информацию из api
@dataclass
class MyDataClass:
    # Метод, который возвращает словарь, соответствующий данному дата-классу
    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}


# Полученная информация о погоде
@dataclass
class WeatherInfo(MyDataClass):
    weather_description: str = ''
    current_temp: str = ''
    current_temp_feels_like: str = ''
    wind_speed: str = ''
    dt: str = ''
    city_name: str = 'Город не указан'

    # Метод, который выводит данные о погоде.
    def print_weather_info(self):
        print('Текущее время:', self.dt)
        print('Название города:', self.city_name)
        print('Погодные условия:', self.weather_description)
        print('Текущая температура:', self.current_temp, 'градусов по цельсию')
        print('Ощущается как:', self.current_temp_feels_like, 'градусов по цельсию')
        print('Скорость ветра:', self.wind_speed, 'м/с')


# Полученная информация по координатам
@dataclass
class Coordinates(MyDataClass):
    lat: float = None
    lon: float = None


class TaskName(StrEnum):
    END = 'Конец'
    GET_WEATHER = 'Получить погоду'
    CITY_BY_COORDS = 'Название города по координатам'
    COORDS_BY_IP = 'Координаты по ip'
    COORDS_BY_CITY = 'Координаты по городу'
    VIEW_HISTORY = 'Посмотреть историю'
    CLEAR_HISTORY = 'Очистить историю'
    PASS = 'Ничего не делать'
    CLOSE_APP = 'Закрыть приложение'


@dataclass
class Task:
    func_name: TaskName


@dataclass
class TaskList:
    WEATER_BY_COORDS_TASKS = [
        Task(func_name=TaskName.CITY_BY_COORDS),
        Task(func_name=TaskName.GET_WEATHER),
        Task(func_name=TaskName.END)
    ]
    WEATER_BY_IP = [
        Task(func_name=TaskName.COORDS_BY_IP),
        Task(func_name=TaskName.GET_WEATHER),
        Task(func_name=TaskName.END)
    ]
    WEATER_BY_CITY_NAME = [
        Task(func_name=TaskName.COORDS_BY_CITY),
        Task(func_name=TaskName.GET_WEATHER),
        Task(func_name=TaskName.END)
    ]
    CLEAR_HISTORY = [
        Task(func_name=TaskName.CLEAR_HISTORY)
    ]
    VIEW_HISTORY = [
        Task(func_name=TaskName.VIEW_HISTORY)
    ]
    PASS = [
        Task(func_name=TaskName.PASS)
    ]
    CLOSE_APP = [
        Task(func_name=TaskName.CLOSE_APP)
    ]
