from dataclasses import dataclass, asdict
from typing import Optional, Callable
from strenum import StrEnum


class Action(StrEnum):
    END_APP = 'Конец'
    MAIN_MENU = 'Главное меню'
    TEMP_BY_COORDS = 'Выбор температуры по координатам'
    TEMP_BY_CITY_NAME = 'Выбор температуры по городу'
    INPUT_COORDS = 'Ввести координаты'
    INPUT_CITY_NAME = 'Ввести название города'
    TEMP_BY_IP = 'Выбор температуры по текущему местоположению'
    VIEW_HISTORY = 'Посмотреть историю'
    CLEAR_HISTORY = 'Очистить историю'


@dataclass
class Menu:
    number: int
    action_label: str
    action: Action


@dataclass
class Option:
    menu_list: list[Menu]
    head: str = ''
    func: Optional[Callable] = None


@dataclass
class WeatherInfo:
    weather_description: str = ''
    current_temp: str = ''
    current_temp_feels_like: str = ''
    wind_speed: str = ''
    dt: str = ''
    city_name: str = 'Город не указан'

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}

    def print_weather_info(self):
        """
        Метод, который выводит данные о погоде.
        """
        print('Текущее время:', self.dt)
        print('Название города:', self.city_name)
        print('Погодные условия:', self.weather_description)
        print('Текущая температура:', self.current_temp, 'градусов по цельсию')
        print('Ощущается как:', self.current_temp_feels_like, 'градусов по цельсию')
        print('Скорость ветра:', self.wind_speed, 'м/с')


@dataclass
class Coordinates:
    lat: float
    lon: float

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
