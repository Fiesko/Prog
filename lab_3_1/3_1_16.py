# Задание task_03_01_16.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241

def pow1(value, power):
    """Вернуть 'value' в степени 'power'.

    Параметры:
        - value: число, которое нужно возвести в степень (int или float).
        - power: степень, в которую нужно возвести число (неотрицательное целое число).

    Результат:
        - value ** power.
    """
    result = 1
    for _ in range(power):
        result *= value
    return result


def pow2(value, power):
    """Вернуть 'value' в степени 'power'. Рекурсивный алгоритм.

    Параметры:
        - value: число, которое нужно возвести в степень (int или float).
        - power: степень, в которую нужно возвести число (неотрицательное целое число).

    Результат:
        - value ** power.
    """
    if power == 0:
        return 1
    else:
        return value * pow2(value, power - 1)


print(pow1(5, 3))
print(pow2(5, 3))

# --------------
# Пример вывода:
#
# 125
# 125