# Задание task_03_02_08.
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241


import random
import time


def timeit(func, *args, **kw):
    """Выполнить функицю 'func' с параметрами '*args', '**kw' и
    вернуть время выполнения в мс."""

    time_start = time.time()
    res = func(*args, **kw)
    time_end = time.time()

    return (time_end - time_start) * 1000.0, res


def maxmin1(data):
    """Вернуть минимум и максимум из 'data'.

    Алгоритм:
        Последовательный перебор всего массива.

    Сложность: !!!.

    Параметры:
        - data (list of int): список целых чисел.

    Результат:
        tuple: мин. и макс. значения."""

    if not data:
        return (None, None)

    min_val = max_val = data[0]
    for num in data[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return (min_val, max_val)


def maxmin2(data):
    """Вернуть минимум и максимум из 'data'.

    Алгоритм:
        Сортировка списка, и возврат первого и последнего элементов.

    Сложность: !!!.

    Параметры:
        - data (list of int): список целых чисел.

    Результат:
        tuple: мин. и макс. значения."""

    if not data:
        return (None, None)

    sorted_data = sorted(data)
    return (sorted_data[0], sorted_data[-1])


def maxmin3(data):
    """Вернуть минимум и максимум из 'data'.

    Алгоритм:
        Используя встроенные функции min() и max().

    Сложность: !!!.

    Параметры:
        - data (list of int): список целых чисел.

    Результат:
        tuple: мин. и макс. значения."""

    if not data:
        return (None, None)

    return (min(data), max(data))

if __name__ == "__main__":
    GEN_LIMIT = 1000000
    dataset = []
    for i in range(4, 7):
        dataset.append(random.sample(range(-GEN_LIMIT, GEN_LIMIT), 10**i))

    res = [["i", "1 способ (мс.)", "2 способ (мс.)", "3 способ (мс.)"]]
    for data in dataset:
        res.append([len(data),
                   timeit(maxmin1, data)[0],
                   timeit(maxmin2, data)[0],
                   timeit(maxmin3, data)[0]])

    # Вывод
    print("{:>15} {:>15} {:>15} {:>15}".format(*res[0]))
    for r in res[1:]:
        print("{:>15} {:>15.2f} {:>15.2f} {:>15.2f}".format(*r))

# -------------
# Пример вывода:
#
#              i  1 способ (мс.)  2 способ (мс.)  3 способ (мс.)
#          10000            1.00            5.00            0.00
#            ...
     