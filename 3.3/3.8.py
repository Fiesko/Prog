
# Задание task_03_03_08.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241



"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""


# Дан список ФИО. Найти наиболее часто встречаемое отчество.
# Если отчества нет, человек не учитывается в подсчете.

n = int(input("Введите кол-во человек: "))

middle_names = {}
for i in range(n):
    fio = input("Введите ФИО через пробел: ").split()

    middle_name = fio[2]
    middle_names[middle_name] = middle_names.get(middle_name, 0) + 1

print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
print("В расчете участвовало человек:", n)


"""
Ошибки (номера строк через пробел, данная строка - №2): 4 8 10 13
"""


# Дан список ФИО. Найти наиболее часто встречаемое отчество.
# Если отчества нет, человек не учитывается в подсчете.

try:
    n = int(input("Введите кол-во человек: "))
    if n <= 0:
        raise ValueError("Количество человек должно быть положительным числом")
    
    middle_names = {}
    valid_count = 0
    
    for i in range(n):
        try:
            fio = input("Введите ФИО через пробел: ").split()
            if len(fio) < 3:
                continue
                
            middle_name = fio[2]
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
            valid_count += 1
            
        except IndexError:
            continue
    
    if not middle_names:
        print("Нет данных для анализа (ни у кого не было отчества)")
    else:
        most_common = sorted(middle_names.items(), key=lambda item: item[1])[-1][0]
        print(f"Наиболее часто встречаемое отчество: {most_common}")
        print("В расчете участвовало человек:", valid_count)

except ValueError as ve:
    print(f"Ошибка ввода числа: {ve}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")