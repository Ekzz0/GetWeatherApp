import requests
from .constants import URL_IPINFO, ULR_GEOCODING_REVERSE_API, ULR_GEOCODING_API, ULR_WEATHER_API, API_KEY, \
    dict_with_geocoding_info


def request_get_loc_by_ip() -> requests.Response:
    """
    Запрос на ipinfo для получения данных по ip адресу
    :return: requests.Response
    """
    response = requests.get(URL_IPINFO)
    return response


def request_get_geocoding_reverse(lat: float | int, lon: float | int) -> requests.Response:
    """
    Запрос на Geocoding reverse API
    :param lat: широта
    :param lon: долгота
    :return: requests.Response
    """
    response = requests.get(ULR_GEOCODING_REVERSE_API,
                            params={'lat': lat, 'lon': lon, 'appid': API_KEY, 'limit': 1})
    return response


def request_get_geocoding(city_name: str) -> requests.Response:
    """
    Запрос на Geocoding API
    :param city_name: название города
    :return: requests.Response
    """
    response = requests.get(ULR_GEOCODING_API,
                            params={'q': city_name, 'appid': API_KEY, 'limit': 1})
    return response


def request_get_weather_map(report_geo: dict_with_geocoding_info) -> requests.Response:
    """
    Запрос на OpenWeatherMap API
    :param report_geo: dict_with_geocoding_info
    :return: requests.Response
    """
    response = requests.get(ULR_WEATHER_API,
                            params={'lat': report_geo['lat'], 'lon': report_geo['lon'],
                                    'appid': API_KEY, 'lang': "ru", "units": 'metric'
                                    }
                            )
    return response
