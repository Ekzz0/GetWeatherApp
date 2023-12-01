from .action_router import TaskManager
from .io_scripts import clear_menu


class MenuInterface:
    def __init__(self):
        self.manager = TaskManager()
        self.options = self.manager.get_options()

    # Цикл с отображением меню по указанными возможными действиям и заголовку.
    def loop(self):
        while True:
            # Вывод заголовка, пунктов меню и выполнение указанной функции
            self.do_current_action()

            # Выбор следующего действия (меню)
            self.select_mode()

    # Отображение заголовка, выполнение указанной в options функции и отображение доступных действий.
    def do_current_action(self):
        # Очистка консоли и отображение заголовка
        clear_menu()

        # Отображение соответствующего заголовка
        if self.options.head:
            print(self.options.head)

        # Вызов соответствующей функции
        if self.options.func:
            func = self.options.func
            func(self.options.args, self.options.methods)

        # Вывод в консоль доступных действий
        self.print_options()

    # Метод, который выводит в консоль данные возможных действий.
    def print_options(self):
        print()
        for menu in self.options.menu_list:
            print(f'{menu.number}: {menu.action_label}', end='')
        print()

    # Выбор следующего действия.
    def select_mode(self):
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
            self.options = self.manager.get_options(action=action)
