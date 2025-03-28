# Задание task_02_25.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241


n = int(input("n = "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} × {j} = {i * j:2}", end="  ")
    print()

# --------------
# Пример вывода:
#
# n = 5
# 1 * 1 =  1  1 * 2 =  2  1 * 3 =  3  1 * 4 =  4  1 * 5 =  5
# 2 * 1 =  2  2 * 2 =  4  2 * 3 =  6  2 * 4 =  8  2 * 5 = 10
# 3 * 1 =  3  3 * 2 =  6  3 * 3 =  9  3 * 4 = 12  3 * 5 = 15
# 4 * 1 =  4  4 * 2 =  8  4 * 3 = 12  4 * 4 = 16  4 * 5 = 20
# 5 * 1 =  5  5 * 2 = 10  5 * 3 = 15  5 * 4 = 20  5 * 5 = 25