# Задание task_03_01_09.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241

LETTERS_EX = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
DIGITS_EX = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

def to_base(number, base):
    """Преобразовать десятичное число 'number' в с.с. 'base'.

    Параметры:
        number (int): десятичное число;
        base (int): система счисления.

    Результат:
        str: число в с.с. 'base'."""
    if number == 0:
        return "0"
    
    result = []
    is_negative = False
    
    if number < 0:
        is_negative = True
        number = abs(number)
    
    while number > 0:
        remainder = number % base
        if remainder >= 10:
            result.append(LETTERS_EX[remainder])
        else:
            result.append(str(remainder))
        number = number // base
    
    if is_negative:
        result.append("-")
    
    return "".join(reversed(result))

def from_base(number, base):
    """Преобразовать число 'number' из с.с. 'base' в 10-ю.

    Параметры:
        number (str): число в исходной системе счисления;
        base (int): система счисления исходного числа.

    Результат:
        int: число в 10-й с.с."""
    if not number:
        return 0
    
    is_negative = False
    if number[0] == "-":
        is_negative = True
        number = number[1:]
    
    result = 0
    for i, digit in enumerate(reversed(number.upper())):
        if digit.isalpha():
            value = DIGITS_EX[digit]
        else:
            value = int(digit)
        result += value * (base ** i)
    
    return -result if is_negative else result


print(to_base(255, 16))  
print(from_base("FF", 16))  
print(to_base(10, 2))  
print(from_base("1010", 2))  