from .constants import dict_with_geocoding_info, dict_with_weather_info
import requests
import datetime


def date_processing(dt: int, timedelta: int) -> str:
    """
    Формирование времени запроса с разницей по UTC
    :param dt: время запроса из API
    :param timedelta: timedelta из API
    :return: время запроса с разницей по UTC
    """
    timezone = datetime.timezone(datetime.timedelta(seconds=float(timedelta)))
    return str(datetime.datetime.fromtimestamp(float(dt), timezone))


def response_processing_weather_map(response: requests.Response, city_name: str) -> dict_with_weather_info:
    """
    Обработка данных из запроса на OpenWeatherMap API
    :param response: запрос на OpenWeatherMap API
    :param city_name: название города
    :return: dict_with_weather_info
    """
    data = response.json()

    weather_description = data['weather'][0]["description"]
    current_temp = data['main']["temp"]
    current_temp_feels_like = data['main']["feels_like"]
    wind_speed = data['wind']['speed']
    dt = date_processing(data["dt"], data["timezone"])

    # Формирование отчета
    report = {"city_name": city_name,
              "weather_description": weather_description,
              "current_temp": current_temp,
              "current_temp_feels_like": current_temp_feels_like,
              "wind_speed": wind_speed,
              'dt': dt
              }

    return report


def response_processing_geocoding(response: requests.Response, city_name: str) -> dict_with_geocoding_info:
    """
    Обработка данных из запроса на geocoding API
    :param response: запрос на Geocoding API
    :param city_name: название города
    :return: dict_with_geocoding_info
    """
    data = response.json()[0]
    lat = data['lat']
    lon = data['lon']

    # Формирование отчета
    report = {'lat': lat, 'lon': lon, 'city_name': city_name}

    return report


def response_processing_geocoding_reverse(response: requests.Response) -> str:
    """
    Обработка данных из запроса на geocoding reverse API
    :param response: запрос на Geocoding API
    :return: определенное название города
    """
    data = response.json()[0]
    name = data['name']

    return name


def response_processing_loc_by_ip(response: requests.Response) -> dict_with_geocoding_info:
    """
    Обработка данных из запроса на ipinfo
    :param response: запрос на ipinfo
    :return: dict_with_geocoding_info
    """
    data = response.json()
    lat, lon = map(float, data['loc'].split(','))
    city_name = data['city']

    return {'lat': lat, 'lon': lon, 'city_name': city_name}
