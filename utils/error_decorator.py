import requests
from typing import Callable


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
