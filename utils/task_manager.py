from .config import WeatherInfo, Coordinates
from .io_scripts import clear_menu
from .routers import functions_router


class TaskManager:
    def __init__(self):
        self.Weather = WeatherInfo()
        self.Coords = Coordinates()
        self.func = None

    def do_tasks(self, tasks):
        for task in tasks:
            function = functions_router.select(task.func_name)
            clear_menu()
            try:
                function(self)
            except Exception as e:
                clear_menu()
                print('Что-то пошло не так.')
            else:
                clear_menu()
