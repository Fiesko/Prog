# Задание task_03_02_10
#
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


def top3_1(db):
    """Вернуть список из ТОП-3 клиентов по сумме активов.

    Алгоритм:
        Сортировка (встроенный метод sort()) и возврат 3-х элементов.

    Сложность: O(n log n).

    Параметры:
        - db (list of dict): список клиентов.

    Результат:
        tuple of dict: 3 клиента с максимальной суммой активов."""
    db_sorted = sorted(db, key=lambda x: x['assets'], reverse=True)
    return tuple(db_sorted[:3])


def top3_2(db):
    """Вернуть список из ТОП-3 клиентов по сумме активов.

    Алгоритм:
        Прямой перебор (1 проход в цикле).

    Сложность: O(n).

    Параметры:
        - db (list of dict): список клиентов.

    Результат:
        tuple of dict: 3 клиента с максимальной суммой активов."""
    top = [{'client_id': 0, 'assets': -1}] * 3
    for client in db:
        if client['assets'] > top[0]['assets']:
            top[2] = top[1]
            top[1] = top[0]
            top[0] = client
        elif client['assets'] > top[1]['assets']:
            top[2] = top[1]
            top[1] = client
        elif client['assets'] > top[2]['assets']:
            top[2] = client

    return tuple(top)


if __name__ == "__main__":
    print("Загрузка базы данных... ")

    GEN_LIMIT = 10000000

    db = []
    for client_id, assets in enumerate(
      random.sample(range(0, 10 * GEN_LIMIT), GEN_LIMIT),
      start=1):
        db.append(dict(client_id=client_id, assets=assets))

    print("Загружено записей: {:,}.\n\nПримеры:".format(GEN_LIMIT))
    print("Первый элемент:", db[0])
    print("Последний элемент:", db[-1])
    print("\n")

    res1 = timeit(top3_1, db)
    res2 = timeit(top3_2, db)

    for i, (func_time, res) in enumerate((res1, res2), start=1):
        print("Способ №{}".format(i))
        print("Время: {:.2f} мс.".format(func_time))
        for j, client in enumerate(res, start=1):
            print("{}-е место: ID={client_id} Активы={assets:,} руб.".
                  format(j, **client))
        print()


# -------------
# Пример вывода:
#
# Загрузка базы данных...
# Загружено записей: 10,000,000.
#
# Примеры:
# Первый элемент: {'client_id': 1, 'assets': 79149360}
# Последний элемент: {'client_id': 10000000, 'assets': 92745004}
#
#
# Способ №1
# Время: 16779.14 мс.
# 1-е место: ID=1346588 Активы=99,999,995 руб.
# 2-е место: ID=9924557 Активы=99,999,979 руб.
# 3-е место: ID=2904705 Активы=99,999,967 руб.
#
# Способ №2
# Время: 4364.90 мс.
# 1-е место: ID=1346588 Активы=99,999,995 руб.
# 2-е место: ID=9924557 Активы=99,999,979 руб.
# 3-е место: ID=2904705 Активы=99,999,967 руб.