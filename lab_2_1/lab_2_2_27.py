
# Задание task_02_27.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241



n = int(input("n = "))
a = []
number = 2

while len(a) < n:
    list_a = True
    i = 2
    while i <= number**0.5:
        if number % i == 0:
            list_a = False
            break
        i += 1
    if list_a:
        a.append(number)
    number += 1

print(" ".join(map(str, a)))


# --------------
# Пример вывода:
#
# n = 10
# 2 3 5 7 11 13 17 19 23 29