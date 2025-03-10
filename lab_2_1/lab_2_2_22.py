# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_02_22.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241


n = int(input("n = "))
count = 0
x = []
for i in range(n):
    count+=1
    a = float(input("{}-е число = ".format(count)))
    x.append(a)


a_max = round(max(x),2)
a_min = round(min(x),2)



print("Максимум: {:.2f}".format(a_max))
print("Минимум: {:.2f}".format(a_min))

# --------------
# Пример вывода:
#
# n = 4
# 1-е число = 6.2
# 2-е число = 3.8
# 3-е число = 1.1
# 4-е число = 9.66
# Максимум: 9.66
# Минимум: 1.10