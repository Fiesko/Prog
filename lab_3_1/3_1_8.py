
# Задание task_03_01_08.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241




def print_with_border(string, char):
    """!!!"""
    border = char * (len(string) + 2)
    print(border)
    print(f"{char}{string}{char}")
    print(border)
    

s = str(input("Введите строку: "))
k = input("введите символ: ")
print_with_border(s,k)

# --------------
# Пример вывода:
#
# Введите строку: Просто текст
# Введите символ: +
# ++++++++++++++
# +Просто текст+
# ++++++++++++++