
# Задание task_03_03_06.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241



"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""


def unemployment_rate(unemployed, employed):
    """Вернуть уровень безработицы (УБ) в долях 1.

       Расчет по формуле: УБ = Безработные / (Занятые + Безработные).
    """
    return unemployed / (unemployed + employed)


unemployed = int(input("Введите кол-во безработных (чел.): "))
employed = int(input("Введите кол-во занятых (чел.): "))
rate = unemployment_rate(unemployed, employed)
print("Уровень безработицы = {:.1%}".format(rate))

"""
Ошибки (номера строк через пробел, данная строка - №2): 12 13 14
"""



def unemployment_rate(unemployed, employed):
    """Вернуть уровень безработицы (УБ) в долях 1.

       Расчет по формуле: УБ = Безработные / (Занятые + Безработные).
    """
    try:
        return unemployed / (unemployed + employed)
    except ZeroDivisionError:
        print("Ошибка: сумма занятых и безработных не может быть нулем!")
        return None
    except TypeError:
        print("Ошибка: введенные значения должны быть числами!")
        return None


try:
    unemployed = int(input("Введите кол-во безработных (чел.): "))
    employed = int(input("Введите кол-во занятых (чел.): "))
    rate = unemployment_rate(unemployed, employed)
    if rate is not None:
        print("Уровень безработицы = {:.1%}".format(rate))
except ValueError:
    print("Ошибка: введите целые числа для количества безработных и занятых!")