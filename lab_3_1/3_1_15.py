# Задание task_03_01_15.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241

def gdp(c, i, g, ex, im):
    """Вернуть значение ВВП.

    Параметры:
        - c: конечное потребление
        - i: валовое накопление капитала
        - g: государственные расходы
        - ex: экспорт
        - im: импорт

    Результат:
        - значение ВВП
    """
    return c + i + g + ex - im


c = int(input("Конечное потребление: "))
i = int(input("Валовое накопление капитала: "))
g = int(input("Государственные расходы: "))
ex = int(input("Экспорт: "))
im = int(input("Импорт: "))

info_dict = {'c': c, 'i': i, 'g': g, 'ex': ex, 'im': im}
info_list = [c, i, g, ex, im]

gdp_from_list = gdp(*info_list)
gdp_from_dict = gdp(**info_dict)

print(f"ВВП = {gdp_from_list}")
print(f"ВВП = {gdp_from_dict}")

# --------------
# Пример вывода:
#
# Конечное потребление: 100
# Валовое накопление капитала: 200
# Государственные расходы: 300
# Экспорт: 400
# Импорт: 500
# ВВП = 500
# ВВП = 500