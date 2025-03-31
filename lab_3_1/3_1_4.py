

# Задание task_03_01_04.
#
# Выполнил: Малеванный И.Б
# Группа: ЦИБ - 241



def is_leap(year):
    """Является ли 'year' високосным годом?

    Параметры:
        .

    Результат:
        bool: True - да, False - нет.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def days(month, year):
    """Вернуть количество дней в месяце 'month' года 'year'.

    Параметры:
        !!!.

    Результат:
        !!!.
    """
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def previous_date(day, month, year):
    """Вернуть день, месяц, год предыдущего дня.

    Параметры:
        !!!.

    Результат:
        !!!.
    """
    if day == 1:
        if month == 1:
            return 31, 12, year - 1
        else:
            prev_month = month - 1
            prev_day = days(prev_month, year)
            return prev_day, prev_month, year
    else:
        return day - 1, month, year


def next_date(day, month, year):
    """Вернуть день, месяц, год следующего дня.

    Параметры:
        !!!.

    Результат:
        !!!.
    """
    days_in_month = days(month, year)
    if day == days_in_month:
        if month == 12:
            return 1, 1, year + 1
        else:
            return 1, month + 1, year
    else:
        return day + 1, month, year


day, month, year =  map(int, input("День, месяц, год через пробел: ").split())
prev_day, prev_month, prev_year = previous_date(day, month, year)
next_day, next_month, next_year = next_date(day, month, year)

print(f"Предыдущий день: {prev_day:02d}/{prev_month:02d}/{prev_year}")
print(f"Следующий день: {next_day:02d}/{next_month:02d}/{next_year}")

# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 3 2000
# Предыдущий день: 29/02/2000
# Следующий день: 02/03/2000