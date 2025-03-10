
# Задание task_02_19.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241



a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

for i in range(a,b+1):
    if i % c == 0:
        print(i,end=" ")

# --------------
# Пример вывода:
#
# a = 1
# b = 10
# c = 2
# 2 4 6 8 10