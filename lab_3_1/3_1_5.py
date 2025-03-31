# Задание task_03_01_05.
#
# Выполнил: Малеванный И.Б
# Группа: ЦИБ - 241

def is_leap(year):
    """Является ли 'year' високосным годом?

    Параметры:
        year (int): Год.

    Результат:
        bool: True - да, False - нет.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days(month, year):
    """Вернуть количество дней в месяце 'month' года 'year'.

    Параметры:
        - month (int): Месяц.
        - year (int): Год.

    Результат:
        int: Количество дней в месяце.
    """
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def another_date(day, month, year, delta=1):
    """Вернуть день, месяц, год, отличающийся на 'delta' дней.

    Параметры:
        - day (int): День.
        - month (int): Месяц.
        - year (int): Год.
        - delta (int): Количество дней для добавления (положительное) или вычитания (отрицательное).

    Результат:
        (day, month, year) новой даты.
    """

    def previous_date(day, month, year):
        """Вернуть день, месяц, год предыдущего дня.

        Параметры:
            - day (int): День.
            - month (int): Месяц.
            - year (int): Год.

        Результат:
            (day, month, year) предыдущего дня.
        """
        if day > 1:
            return day - 1, month, year
        else:
            if month == 1:
                return 31, 12, year - 1
            else:
                prev_month = month - 1
                prev_days = days(prev_month, year)
                return prev_days, prev_month, year


    def next_date(day, month, year):
        """Вернуть день, месяц, год следующего дня.

        Параметры:
            - day (int): День.
            - month (int): Месяц.
            - year (int): Год.

        Результат:
            (day, month, year) следующего дня.
        """
        days_in_month = days(month, year)
        if day < days_in_month:
            return day + 1, month, year
        else:
            if month == 12:
                return 1, 1, year + 1
            else:
                return 1, month + 1, year


    current_day, current_month, current_year = day, month, year

    if delta > 0:
        for _ in range(delta):
            current_day, current_month, current_year = next_date(current_day, current_month, current_year)
    elif delta < 0:
        for _ in range(abs(delta)):
            current_day, current_month, current_year = previous_date(current_day, current_month, current_year)

    return current_day, current_month, current_year

day, month, year = map(int, input("День, месяц, год через пробел: ").split())
delta = int(input("Сдвиг (может быть отрицательным): "))

new_day, new_month, new_year = another_date(day, month, year, delta)
print(f"Новый день: {new_day:02d}/{new_month:02d}/{new_year}")

# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): -2
# Новый день: 30/12/1999
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): 2
# Новый день: 03/01/2000