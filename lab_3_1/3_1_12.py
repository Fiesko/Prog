# Задание task_03_01_12.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241

# В данной задаче ввод с клавиатуры не нужен.
#
# Используйте пример данных ниже, при необходимости измените его для
# проверки правильности решения

data = [
    {1: 'м', 2: 'м', 3: 'м', 4: 'ж'},
    {1: 'ж', 2: 'м', 3: 'ж', 4: 'ж'},
    {1: 'ж', 2: 'ж', 3: 'ж', 4: 'ж'},
    {1: 'м', 2: 'м', 3: 'м', 4: 'м'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: 'м', 3: None, 4: 'м'},
    {1: 'ж', 2: None, 3: None, 4: 'ж'}
]


def vacant_compartments(data):
    """Вернуть список полностью свободных купе. Нумерация купе идет с 1.

    Параметры:
        - data (list of dict): данные о занятости мест в вагоне.

    Результат:
        list of int."""
    result = []
    for i, compartment in enumerate(data, 1):
        if all(value is None for value in compartment.values()):
            result.append(i)
    return result


def vacant_seats(data, compartments_condition=None, seat_condition=None):
    """Вернуть список свободных мест при соблюдении условий
    'compartments_condition' и 'seat_condition'.
    Нумерация купе и мест идет с 1.

    Параметры:
        - data (list of dict): данные о занятости мест в вагоне;
        - compartments_condition (function):
          функция c 1 параметром (словарь - купе), возвращающая True/False;
        - seat_condition (function):
          функция c 2 параметрами (номер места, значение),
          возвращающая True/False.

    Результат:
        list of tuple: список кортежей вида (номер купе, номер места)."""
    result = []
    for compartment_num, compartment in enumerate(data, 1):
        if compartments_condition is None or compartments_condition(compartment):
            for seat, value in compartment.items():
                if value is None and (seat_condition is None or seat_condition(seat, value)):
                    result.append((compartment_num, seat))
    return result


def is_same_sex_and_vacant(compartment, sex):
    """Вернуть True, если в купе 'compartment' есть свободные места,
    а остальные пассажиры только пола 'sex'.

    Параметры:
        - compartment (dict): данные о купе;
        - sex (str): пол ("м" или "ж").

    Результат:
        bool."""
    has_vacant = any(value is None for value in compartment.values())
    if not has_vacant:
        return False
    for value in compartment.values():
        if value is not None and value != sex:
            return False
    return True


print(vacant_compartments(data))
print(vacant_seats(data))
print(vacant_seats(data, seat_condition=lambda seat, value: seat % 2 != 0))
print(vacant_seats(data, seat_condition=lambda seat, value: seat % 2 == 0))
print(vacant_seats(data, lambda x: is_same_sex_and_vacant(x, "м")))
print(vacant_seats(data, lambda x: is_same_sex_and_vacant(x, "ж")))


# --------------
# Пример вывода:
#
# [5, 7]
# [(5, 1), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3),
#  (7, 4), (8, 3), (9, 2), (9, 3)]
# [(5, 1), (5, 3), (6, 3), (7, 1), (7, 3), (8, 3), (9, 3)]
# [(5, 2), (5, 4), (6, 2), (7, 2), (7, 4), (9, 2)]
# [(8, 3)]
# [(9, 2), (9, 3)]