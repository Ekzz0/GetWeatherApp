from .getters import get_location_by_ip, get_coordinates_reverse, get_coordinates, \
    get_weather
from .errors_processing import requests_errors
from .io_scripts import input_coords, clear_menu
from .config import WeatherInfo, Coordinates


@requests_errors
def coordinates_by_city_name() -> tuple[Coordinates, WeatherInfo]:
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
        except IndexError:
            # Обработка ошибки, связанной с неверно введенным названием
            clear_menu()
            print("Вы неверно ввели название города. Попробуйте еще раз\n")
        else:
            return Coords, WeatherInfo(city_name=city_name)


@requests_errors
def city_name_by_coordinates(Coords: Coordinates) -> WeatherInfo | str:
    """
    Получение названия города по координатам (lat, lon)
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


@requests_errors
def weather_by_entered_coordinates() -> WeatherInfo:
    """
    Получение прогноза погоды по введенным координатам (lat, lon)
    :return: прогноз погоды
    """
    Coords = input_coords()
    Weather = city_name_by_coordinates(Coords)
    Weather = get_weather(Coords, Weather)

    return Weather


@requests_errors
def weather_by_received_coordinates(Coords, Weather) -> WeatherInfo:
    """
    Получение прогноза погоды (Weather) по полученным координатам (lat, lon)
    :return: Weather
    """
    Weather = get_weather(Coords, Weather)

    return Weather


@requests_errors
def coordinates_by_ip():
    """
    Получение координат по текущему местоположению
    :return: координаты и Weather с названием города
    """
    Coords, Weather = get_location_by_ip()

    return Coords, Weather
