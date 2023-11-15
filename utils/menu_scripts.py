from .actions_menu import get_options_by_action_name
from .io_scripts import clear_menu
from .constants import dict_with_action_options


def print_options(options: dict_with_action_options):
    """
    Метод, который выводит в консоль данные возможных действий.
    :param options: словарь с информацией о доступных в данном меню действиях.
    """
    # Try-except использован для того, чтобы выводить в консоль только те элементы словаря options,
    # которые имею ключ - целое число, т.к. в словаре хранятся и значения с ключами другого формата

    for menu in options.menu_list:
        print(f'{menu.number}: {menu.action_label}', end='')
    print()


def print_head_and_options(options: dict_with_action_options):
    """
    Отображение заголовка, выполнение указанной в options функции и отображение доступных действий.
    :param options: словарь с информацией о доступных в данном меню действиях.
    """
    # Очистка консоли и отображение заголовка
    clear_menu()
    if options.head:
        print(options.head)

    # Вызов соответствующей функции
    if options.func:
        func = options.func
        func()

    # Вывод в консоль доступных действий
    print_options(options)


def loop(options: dict_with_action_options):
    """
    Отображение меню по указанным возможным действиям и заголовку.
    :param options: словарь с информацией о доступных в данном меню действиях.
    """
    while True:
        # Вывод заголовка и пунктов меню
        print_head_and_options(options)

        # Выбор следующего действия (меню)
        options = select_mode(options)


def select_mode(options: dict_with_action_options) -> dict_with_action_options:
    """
    Выбор следующего действия.
    :param options: словарь с информацией о доступных в данном меню действиях.
    :return: словарь с информацией о доступных в данном меню действиях.
    """
    try:
        # Выбор действия
        mode = int(input("Выберите действие (введите цифру): ").strip())
        action = options.menu_list[mode - 1].action
    except ValueError:
        # Обработка ошибки, связанной с неверно выбранным меню
        clear_menu()
        options.func = None
        return options
    except KeyError:
        # Обработка ошибки, связанной с неверно выбранным меню
        clear_menu()
        options.func = None
        return options
    else:
        clear_menu()
        # Получение параметров выбранного меню
        options = get_options_by_action_name(action)
        return options
