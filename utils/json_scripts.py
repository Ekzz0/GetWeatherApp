import json
from .data_structures import WeatherInfo


def fill_json(data: WeatherInfo):
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
            json.dump(data.dict(), file)  # записываем структуру в файл
            file.write(']')


def read_json(filename: str) -> list[dict]:
    """
    Метод для чтения json файла
    :param filename: имя открываемого файла
    :return: dict_with_weather_info
    """
    with open(filename, "r") as file:
        data = json.load(file)

    return data
