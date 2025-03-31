# Задание task_03_01_14.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241

def split_numbers(*args):
    """Вернуть 2 списка - отрицательных и неотицательных значений.

    Аргументы:
        *args: произвольное количество числовых аргументов.

    Результат:
        - list: отрицательные значения;
        - list: неотицательные значения."""
    negative_numbers = [x for x in args if x < 0]
    non_negative_numbers = [x for x in args if x >= 0]
    
    negative_numbers.sort(reverse=True)
    
    non_negative_numbers.sort()
    
    return (negative_numbers, non_negative_numbers)


print(split_numbers(1, 4, -5, 0, -33))

# --------------
# Пример вывода:
#
# ([-5, -33], [0, 1, 4])