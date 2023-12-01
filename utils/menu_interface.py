from .routers import options_router
from .task_manager import TaskManager
from .io_scripts import clear_menu


class MenuInterface:
    def __init__(self):
        self.manager = TaskManager()
        self.options = options_router.select()

    # Цикл с отображением меню по указанными возможными действиям и заголовку.
    def loop(self):
        while True:
            # Вывод заголовка, пунктов меню и выполнение указанной функции
            self.__do_current_action()

            # Выбор следующего действия (меню)
            self.__select_mode()

    # Отображение заголовка, выполнение указанной в options функции и отображение доступных действий.
    def __do_current_action(self):
        # Очистка консоли и отображение заголовка
        clear_menu()

        # Отображение соответствующего заголовка
        if self.options.head:
            print(self.options.head)

        # Вызов соответствующей функции
        self.manager.do_tasks(self.options.args)

        # Вывод в консоль доступных действий
        self.__print_options()

    # Метод, который выводит в консоль данные возможных действий.
    def __print_options(self):
        print()
        for menu in self.options.menu_list:
            print(f'{menu.number}: {menu.action_label}', end='')
        print()

    # Выбор следующего действия.
    def __select_mode(self):
        try:
            # Выбор действия
            mode = int(input("Выберите действие (введите цифру): ").strip())
            action = self.options.menu_list[mode - 1].action
        # Обработка ошибки, связанной с неверно выбранным меню
        except (IndexError, ValueError, KeyError):
            clear_menu()
            self.options.func = None
        else:
            clear_menu()
            # Получение параметров выбранного меню
            self.options = options_router.select(action=action)
