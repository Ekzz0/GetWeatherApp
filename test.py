
import utils_1 as utils

if __name__ == "__main__":
    # manager = ActionTaskManager(TaskList.WEATER_BY_COORDS_TASKS)
    # manager.do_tasks().print_weather_info()

    # Объявление интерфейса
    Menu = utils.MenuInterface()

    # Запуск консольного приложения
    Menu.loop()
    # lat = 1
    # lon = 1
    # a = ActionTasksMethods()
    # a.Coords = Coordinates(lat=lat, lon=lon)
    # a.get_weather()
    # print(a.Weather.print_weather_info())
