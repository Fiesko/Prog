
# Задание task_03_01_06.
#
# Выполнил: Малеванный И.Б
# Группа: ЦИБ - 241



def gcd(first, second):
    """Вернуть НОД целых чисел 'first' и 'second'."""
    while second:
        first, second = second, first % second
    return abs(first)


def lcm(first, second):
    """Вернуть НОК целых чисел 'first' и 'second'."""
    return abs(first * second) // gcd(first, second) if first and second else 0


def gcd_nums(nums):
    """Вернуть НОД чисел из списка 'nums'.

    Параметры:
        !!!.

    Результат:
        !!!.
    """
    if not nums:
        return 0
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result


def lcm_nums(nums):
    """Вернуть НОК чисел из списка 'nums'.

    Параметры:
        !!!.

    Результат:
        !!!.
    """
    if not nums:
        return 0
    result = nums[0]
    for num in nums[1:]:
        result = lcm(result, num)
    return result


nums = list(map(int, input("Введите числа через пробел: ").split()))

print(f"НОД = {gcd_nums(nums)}")
print(f"НОК = {lcm_nums(nums)}")

# --------------
# Пример вывода:
#
# Введите числа через пробел: 8 10 14
# НОД = 2
# НОК = 280
#
# Введите числа через пробел: 6 8 24 16
# НОД = 2
# НОК = 48