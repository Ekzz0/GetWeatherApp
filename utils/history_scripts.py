import json
import traceback

from .config import PATH_HISTORY
from .json_scripts import read_json
from .io_scripts import clear_menu, input_count, print_row_from_json


# Алгоритм действия 'Очистить историю'
def clear_history(*args, **kwargs):
    with open(PATH_HISTORY, 'w'):
        pass


# Алгоритм действия 'Посмотреть историю'
def data_from_history(*args, **kwargs):
    try:
        data = read_json(PATH_HISTORY)
    except json.decoder.JSONDecodeError:
        clear_menu()
        print("Файл пуст.")
    else:
        print("Количество записей в истории:", len(data))
        count = input_count()
        clear_menu()
        try:
            if count > len(data):
                clear_menu()
                print(f"Количество записей истории: {len(data)}, что меньше, чем вы хотите получить ({count})."
                      f"\nВывод всех имеющихся:\n")
                # Добавить вывод всех имеющихся
                for i, row in enumerate(data[::-1]):
                    print_row_from_json(i, row)
            else:
                clear_menu()
                for i, row in enumerate(data[::-1][:count]):
                    print_row_from_json(i, row)
        except Exception as e:
            clear_menu()
            print("Неизвестная ошибка:", type(e), e)
            print(traceback.format_exc())

