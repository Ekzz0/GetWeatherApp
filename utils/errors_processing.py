from http import HTTPStatus
import requests


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



