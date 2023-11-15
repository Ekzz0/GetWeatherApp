from .requests_scripts import get_location_by_ip, get_coordinates_reverse, get_coordinates, \
    get_weather
from .errors_processing import requests_errors
from .io_scripts import get_coords_by_console, clear_menu
from .data_structures import WeatherInfo, Coordinates


@requests_errors
def get_coordinates_by_city_name() -> tuple[Coordinates, WeatherInfo]:
    """
    Получение report_geo по названию города (city_name)
    :return: report_geo
    """
    while True:
        city_name = input("Введите название города: ").strip()
        try:
            # Получение координат
            Coords = get_coordinates(city_name)
            clear_menu()
        except IndexError:
            # Обработка ошибки, связанной с неверно введенным названием
            clear_menu()
            print("Вы неверно ввели название города. Попробуйте еще раз\n")
        else:
            return Coords, WeatherInfo(city_name=city_name)


def get_city_name_by_coordinates(Coords: Coordinates) -> WeatherInfo | str:
    """
    Получение названия города (city_name) по координатам (lat, lon)
    :return: city_name
    """
    try:
        Weather = get_coordinates_reverse(Coords)
    except IndexError:
        return 'Город не указан'
    except KeyError:
        return 'Город не указан'
    else:
        return Weather


def get_weather_by_coordinates() -> WeatherInfo:
    """
    Получение прогноза погоды (report_weather) по координатам (lat, lon)
    :return: report_weather
    """
    Coords = get_coords_by_console()
    Weather = get_city_name_by_coordinates(Coords)
    Weather = get_weather(Coords, Weather)

    return Weather


@requests_errors
def get_weather_by_location(Coords, Weather) -> WeatherInfo:
    """
    Получение прогноза погоды (Weather) по report_geo
    :return: Weather
    """
    Weather = get_weather(Coords, Weather)

    return Weather


@requests_errors
def get_coordinates_by_ip():
    """
    Получение report_geo по текущему местоположению
    :return: report_geo
    """
    Coordinates, Weather = get_location_by_ip()

    return Coordinates, Weather
