
# Задание task_02_20.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241



n = int(input('n = '))

for i in range(100,1000):
    last = i % 10
    second = i // 10 % 10
    first = i // 100
    if last + second + first == n:
        print(i,end = " ")

        





# --------------
# Пример вывода:
#
# n = 3
# 102 111 120 201 210 300