import requests
import datetime
from .data_structures import Coordinates, WeatherInfo


def processing_date(dt: int, timedelta: int) -> str:
    """
    Формирование времени запроса с разницей по UTC
    :param dt: время запроса из API
    :param timedelta: timedelta из API
    :return: время запроса с разницей по UTC
    """
    timezone = datetime.timezone(datetime.timedelta(seconds=float(timedelta)))
    return str(datetime.datetime.fromtimestamp(float(dt), timezone))


def processing_weather(response: requests.Response, Weather: WeatherInfo) -> WeatherInfo:
    """
    Обработка данных из запроса на OpenWeatherMap API
    :param Weather:
    :param response: запрос на OpenWeatherMap API
    :return: WeatherInfo
    """
    data = response.json()

    weather_description = data['weather'][0]["description"]
    current_temp = data['main']["temp"]
    current_temp_feels_like = data['main']["feels_like"]
    wind_speed = data['wind']['speed']
    dt = processing_date(data["dt"], data["timezone"])

    # Формирование отчета
    Weather.weather_description = weather_description
    Weather.current_temp = current_temp
    Weather.current_temp_feels_like = current_temp_feels_like
    Weather.wind_speed = wind_speed
    Weather.dt = dt

    return Weather


def processing_coordinates(response: requests.Response) -> Coordinates:
    """
    Обработка данных из запроса на geocoding API
    :param response: запрос на Geocoding API
    :return: Coordinates
    """
    data = response.json()[0]
    lat = data['lat']
    lon = data['lon']

    # Формирование отчета
    return Coordinates(lat=lat, lon=lon)


def processing_coordinates_reverse(response: requests.Response) -> str:
    """
    Обработка данных из запроса на geocoding reverse API
    :param response: запрос на Geocoding API
    :return: определенное название города
    """
    data = response.json()[0]
    name = data['name']

    return name


def processing_location_by_ip(response: requests.Response) -> tuple[Coordinates, WeatherInfo]:
    """
    Обработка данных из запроса на ipinfo
    :param response: запрос на ipinfo
    :return: dict_with_geocoding_info
    """
    data = response.json()
    lat, lon = map(float, data['loc'].split(','))

    return Coordinates(lat=lat, lon=lon), WeatherInfo(city_name=data['city'])
