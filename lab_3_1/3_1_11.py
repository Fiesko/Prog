# Задание task_03_01_11.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241

def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.

    Параметры:
        - text (str): строка;
        - shift (int): сдвиг.

    Результат:
        str: измененная строка."""
    lower_letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    upper_letters = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
    result = []
    
    for char in text:
        if char in lower_letters:
            index = (lower_letters.index(char) + shift) % len(lower_letters)
            result.append(lower_letters[index])
        elif char in upper_letters:
            index = (upper_letters.index(char) + shift) % len(upper_letters)
            result.append(upper_letters[index])
        else:
            result.append(char)
    return ''.join(result)

text = input("Введите предложение: ")
shift = int(input("Введите сдвиг: "))

encoded = ceasar(text, shift)
decoded = ceasar(encoded, -shift) 

print("Зашифрованная строка:", encoded)
print("Расшифрованная строка:", decoded)

# --------------
# Пример вывода:
#
# Введите предложение: ПрограММиРОВание С++
# Введите сдвиг: 4
# Зашифрованная строка: УфтзфдРРмФТЖдсмй Х++
# Расшифрованная строка: ПрограММиРОВание С++