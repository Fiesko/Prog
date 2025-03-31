
# Задание task_03_01_07.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241



def has_digits(sentence):
    """!!!"""
    colvo = 0
    colvo = sentence.count("1")
    return colvo
    


def sentences_with_digits_count(sentences):

    """!!!."""
    count = 0
    for sentence in sentences:
        if has_digits(sentence) > 0:
            count += 1
    return count


n = int(input("Введите количество предложений: "))
sentences_list = []  

for i in range(n):
    sentence = input(f'Введите предложение №{i+1}: ')
    sentences_list.append(sentence)


 

print("Предложения с цифрой =",sentences_with_digits_count(sentences_list))

# --------------
# Пример вывода:
#
# Введите количество предложений: 3
# Введите предложение №1:
# Просто текст
# Введите предложение №2:
# Текст с цифрой 1 (один)
# Введите предложение №3:
# Тут нет цифры
# Предложений с цифрой = 1