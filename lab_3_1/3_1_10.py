
# Задание task_03_01_10.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241




def sentence_stats(sentence):
    """Вернуть символьную статистику 'sentence'. Регистр не учитывается.


    !!!
    """
    stats = {}
    for char in sentence.lower():
          
        if char in stats:
            stats[char] += 1
        else:
            stats[char] = 1
    return stats

s = input("Введите предложение: ")
print(sentence_stats(s))
# --------------
# Пример вывода:
#
# Введите предложение: мама МЫла РамУ
# {'л': 1, 'р': 1, 'у': 1, 'м': 4, 'а': 4, 'ы': 1, ' ': 2}