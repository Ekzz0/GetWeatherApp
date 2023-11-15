from http import HTTPStatus
from typing import Callable
import requests


def requests_errors(func: Callable) -> Callable:
    """
    Метод для отлавливания ошибок типа HTTPError, ConnectionError, Timeout, RequestException
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs) -> Callable:
        try:
            return func(*args, **kwargs)
        except requests.HTTPError:
            quit()
        except requests.ConnectionError:
            print("Ошибка подключения")
            quit()
        except requests.Timeout:
            print("Ошибка тайм-аута")
            quit()
        except requests.RequestException:
            print("Ошибка запроса")
            quit()

    return wrapper

def open_weather_error_processing(cod: int):
    """
    Данный метод отлавливает ошибки, которые могут возникнуть при использовании Open Weather Map API.
    :param cod: код ошибки
    """
    if cod == HTTPStatus.BAD_REQUEST.value:  # 400
        print("Неправильно введены координаты. Попробуйте еще раз")
        raise requests.HTTPError
    elif cod == HTTPStatus.UNAUTHORIZED.value:  # 401
        print("Возникла одна из следующих ошибок:\n"
              "- Вы не указали свой ключ API в запросе API.\n"
              "- Ваш ключ API еще не активирован.\n"
              "- Вы используете неправильный ключ API в запросе API.")
        raise requests.HTTPError
    # elif cod == HTTPStatus.NOT_FOUND.value:  # 404
    #     print("Вы указали неправильное название города. Попробуйте еще раз.\n")
    #     raise requests.HTTPError



