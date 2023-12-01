from .errors_processing import requests_errors
from .requests import request_city_name_by_coordinates, request_weather, request_location_by_ip, request_coordinates
from .io_scripts import input_coords, clear_menu
from .json_scripts import fill_json


@requests_errors
def get_city_name_by_coordinates(self):
    """
    Получение названия города по координатам (lat, lon)
    :return: city_name
    """
    while True:
        self.Coords = input_coords()
        try:
            Weather = request_city_name_by_coordinates(self.Coords)
            clear_menu()
        except (IndexError, KeyError):
            clear_menu()
        else:
            self.Weather = Weather
            return


@requests_errors
def get_weather(self):
    """
    Запрос на OpenWeatherMap API и его обработка
    :param
    :return: WeatherInfo
    """
    self.Weather = request_weather(self.Coords, self.Weather)


@requests_errors
def get_coordinates_by_ip(self):
    """
    Запрос на ipinfo для получения данных по ip адресу и его обработка
    :return: Coordinates, WeatherInfo
    """
    # TODO: Добавить обработку ошибок, связанных с невозможностью получения координат по Ip
    self.Coords, self.Weather = request_location_by_ip()


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
            Coords = request_coordinates(city_name)
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


def void(*args, **kwargs):
    pass

def close(*args, **kwargs):
    quit()