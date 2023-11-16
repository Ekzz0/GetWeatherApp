from .actions_router import get_options_by_action_name
from .io_scripts import clear_menu
from .config import Option


class MenuInterface:
    def __init__(self):
        self.options = get_options_by_action_name()

    def loop(self):
        """
        Отображение меню по указанным возможным действиям и заголовку.
        """
        while True:
            # Вывод заголовка и пунктов меню
            self.print_head_and_options()

            # Выбор следующего действия (меню)
            self.select_mode()

    def print_head_and_options(self):
        """
        Отображение заголовка, выполнение указанной в options функции и отображение доступных действий.
        """
        # Очистка консоли и отображение заголовка
        clear_menu()
        if self.options.head:
            print(self.options.head)

        # Вызов соответствующей функции
        if self.options.func:
            func = self.options.func
            func()

        # Вывод в консоль доступных действий
        self.print_options()

    def print_options(self):
        """
        Метод, который выводит в консоль данные возможных действий.
        """
        for menu in self.options.menu_list:
            print(f'{menu.number}: {menu.action_label}', end='')
        print()

    def select_mode(self):
        """
        Выбор следующего действия.
        :return: словарь с информацией о доступных в данном меню действиях.
        """
        try:
            # Выбор действия
            mode = int(input("Выберите действие (введите цифру): ").strip())
            action = self.options.menu_list[mode - 1].action
        except ValueError:
            # Обработка ошибки, связанной с неверно выбранным меню
            clear_menu()
            self.options.func = None
        except KeyError:
            # Обработка ошибки, связанной с неверно выбранным меню
            clear_menu()
            self.options.func = None
        else:
            clear_menu()
            # Получение параметров выбранного меню
            self.options = get_options_by_action_name(action=action)
