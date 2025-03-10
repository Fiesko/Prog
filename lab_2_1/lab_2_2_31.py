
# Задание task_02_31.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ - 241



s = input("Введите предложение: ")
k = input("Введите букву: ").lower()
words = s.split()
filtered_words = [word for word in words if k not in word.lower()]
result = " ".join(filtered_words)
print(result)

# --------------
# Пример вывода:
#
# Введите предложение = МАМА мыла РаМу
# Введите букву = р
# МАМА мыла