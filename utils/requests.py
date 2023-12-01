import requests
from .config import URLs, WeatherInfo, Coordinates, API_KEY
from .errors_processing import open_weather_error_processing
from .data_processing import processing_weather, processing_coordinates, \
    processing_coordinates_reverse, processing_location_by_ip


def request_location_by_ip() -> tuple[Coordinates, WeatherInfo]:
    """
    Запрос на ipinfo для получения данных по ip адресу и его обработка
    :return: Coordinates, WeatherInfo
    """
    response = requests.get(URLs.URL_IPINFO)
    Coords, Weather = processing_location_by_ip(response)

    return Coords, Weather


def request_city_name_by_coordinates(Coords) -> WeatherInfo:
    """
    Запрос на Geocoding reverse API и его обработка
    :param Coords: широта и долгота
    :return: WeatherInfo
    """
    response = requests.get(URLs.ULR_GEOCODING_REVERSE_API,
                            params={'lat': Coords.lat, 'lon': Coords.lon, 'appid': API_KEY, 'limit': 1})
    Weather = WeatherInfo(city_name=processing_coordinates_reverse(response))
    return Weather


def request_coordinates(city_name: str) -> Coordinates:
    """
    Запрос на Geocoding API и его обработка
    :param city_name: название города
    :return: Coordinates
    """
    response = requests.get(URLs.ULR_GEOCODING_API,
                            params={'q': city_name, 'appid': API_KEY, 'limit': 1})
    # Проверка на ошибки из Open Weather Map
    open_weather_error_processing(response.status_code)
    Coords = processing_coordinates(response)
    return Coords


def request_weather(Coords, Weather) -> WeatherInfo:
    """
    Запрос на OpenWeatherMap API и его обработка
    :param
    :return: WeatherInfo
    """
    response = requests.get(URLs.ULR_WEATHER_API,
                            params={'lat': Coords.lat, 'lon': Coords.lon,
                                    'appid': API_KEY, 'lang': "ru", "units": 'metric'
                                    }
                            )
    open_weather_error_processing(response.status_code)
    Weather = processing_weather(response, Weather)
    return Weather
