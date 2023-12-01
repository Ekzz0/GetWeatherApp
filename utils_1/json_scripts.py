import json
from .config import PATH_HISTORY, WeatherInfo



def fill_json(data: WeatherInfo):
    """
    Метод для заполнения json файла по словарю с данными о погоде.
    :param data: словарь с данными о погоде
    """
    with open(PATH_HISTORY, 'a+') as file:
        try:
            file.seek(file.truncate(file.tell() - 1))  # обрезаем хвост и переходим в конец
            file.write(',\n')  # добавим запятую

        except OSError:
            file.write('[')
        finally:
            json.dump(data.dict(), file)  # записываем структуру в файл
            file.write(']')


def read_json(path: str) -> list[dict]:
    """
    Метод для чтения json файла.
    :param path: путь к файлу.
    :return: список со словарями, которые хранят данные о погоде. Формат словаря такой же, как и WeatherInfo
    """
    with open(path, "r") as file:
        data = json.load(file)

    return data
