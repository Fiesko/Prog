
# Задание task_03_03_07.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241



"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""


def power(x, y=2):
    """Вернуть x^y."""
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


x = int(input("x="))
y = int(input("y="))
print(power(x, y))


"""
Ошибки (номера строк через пробел, данная строка - №2): 12 13 14
"""



def power(x, y=2):
    """Вернуть x^y."""
    if y == 0:
        return 1
    elif y < 0:
        raise ValueError("Отрицательные степени не поддерживаются")
    else:
        return x * power(x, y - 1)


try:
    x = int(input("x="))
    y = int(input("y="))
    if y > 1000:  # Ограничиваем глубину рекурсии
        raise ValueError("Слишком большая степень")
    print(power(x, y))
except ValueError as e:
    print(f"Ошибка ввода: {e}")
except RecursionError:
    print("Ошибка: слишком глубокая рекурсия")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")