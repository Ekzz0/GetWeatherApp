import json
from .constants import dict_with_weather_info


def fill_json(data: dict_with_weather_info):
    """
    Метод для заполнения json файла по словарю с данными о погоде.
    :param data: словарь с данными о погоде
    """
    with open("history/history.json", 'a+') as file:
        try:
            file.seek(file.truncate(file.tell() - 1))  # обрезаем хвост и переходим в конец
            file.write(',\n')  # добавим запятую

        except OSError:
            file.write('[')
        finally:
            json.dump(data, file)  # записываем структуру в файл
            file.write(']')


def read_json(filename: str) -> dict_with_weather_info:
    """
    Метод для чтения json файла
    :param filename: имя открываемого файла
    :return: dict_with_weather_info
    """
    with open(filename, "r") as file:
        data = json.load(file)

    return data
