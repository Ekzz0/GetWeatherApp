from .requests_scripts import request_get_loc_by_ip, request_get_geocoding_reverse, request_get_geocoding,\
    request_get_weather_map
from .data_processing import response_processing_weather_map, response_processing_geocoding,\
    response_processing_geocoding_reverse, response_processing_loc_by_ip
from .errors_processing import open_weather_error_processing
from .error_decorator import requests_errors
from .io_scripts import get_coords_by_console, clear_menu
from .constants import dict_with_weather_info, dict_with_geocoding_info


@requests_errors
def get_report_geo_by_city_name() -> dict_with_geocoding_info:
    """
    Получение report_geo по названию города (city_name)
    :return: report_geo
    """
    city_name = input("Введите название города: ").strip()
    try:
        # Получение координат
        response = request_get_geocoding(city_name)
        clear_menu()
        # Проверка на ошибки из Open Weather Map
        open_weather_error_processing(response.status_code)
        report_geo = response_processing_geocoding(response, city_name)
    except IndexError:
        # Обработка ошибки, связанной с неверно введенным названием
        clear_menu()
        print("Вы неверно ввели название города. Попробуйте еще раз\n")
        report_geo = get_report_geo_by_city_name()
        return report_geo
    else:
        return report_geo


def get_city_name_by_coords(lat: float, lon: float):
    """
    Получение названия города (city_name) по координатам (lat, lon)
    :return: city_name
    """
    try:
        response = request_get_geocoding_reverse(lat, lon)
        city_name = response_processing_geocoding_reverse(response)
    except IndexError:
        return 'Город не указан'
    except KeyError:
        return 'Город не указан'
    else:
        return city_name


def get_report_weather_by_coords() -> dict_with_weather_info:
    """
    Получение прогноза погоды (report_weather) по координатам (lat, lon)
    :return: report_weather
    """
    lat, lon = get_coords_by_console()
    city_name = get_city_name_by_coords(lat, lon)
    report_geo = {'lat': lat, 'lon': lon, 'city_name': city_name}
    report_weather = get_report_weather_by_report_geo(report_geo)

    return report_weather


@requests_errors
def get_report_weather_by_report_geo(report_geo: dict_with_geocoding_info) -> dict_with_weather_info:
    """
    Получение прогноза погоды (report_weather) по report_geo
    :return: report_weather
    """
    response = request_get_weather_map(report_geo)
    open_weather_error_processing(response.status_code)
    city_name = report_geo.get("city_name", "Город не указан")
    report_weather = response_processing_weather_map(response, city_name)

    return report_weather


@requests_errors
def get_report_geo_by_current_geo():
    """
    Получение report_geo по текущему местоположению
    :return: report_geo
    """
    response = request_get_loc_by_ip()
    report_geo = response_processing_loc_by_ip(response)
    report_geo['city_name'] = report_geo['city_name'] + " (Может быть определен не точно из-за ip адреса)"

    return report_geo
