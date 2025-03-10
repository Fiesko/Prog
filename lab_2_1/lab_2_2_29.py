
# Задание task_02_29.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241


n = int(input("n = "))
n_mult = 1
nums = []
for i in range(n):
    num = float(input(f"Введите {i+1}-й элемент списка: "))
    nums.append(num)

nums_pos = [x for x in nums if x > 0]
nums_neg = []
for x in nums:
    if x < 0:
        nums_neg.append(x)

sr_ar = sum(nums_pos) / len(nums_pos)

for i in nums_neg:
    n_mult *= i
sr_geom = (n_mult) ** (1 / len(nums_neg)) 

print("Исходный список:", nums)
print("Положительные числа:", nums_pos)
print("Отрицательные числа:", nums_neg)
print("Ср. арифм.:", round(sr_ar, 2))
print("Ср. геом.:", round(sr_geom, 2))
# --------------
# Пример вывода:
#
# n = 4
# Введите 1-й элемент списка: 1
# Введите 2-й элемент списка: 6
# Введите 3-й элемент списка: -10
# Введите 4-й элемент списка: -3
# Исходный список: [1.0, 6.0, -10.0, -3.0]
# Положительные числа: [1.0, 6.0]
# Отрицательные числа: [-10.0, -3.0]
# Ср. арифм.: 3.50
# Ср. геом.: 5.48