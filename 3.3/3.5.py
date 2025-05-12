
# Задание task_03_03_05.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241




"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""


def non_negatives(nums):
    """Удалить из списка чисел 'nums' отрицательные элементы и вернуть
    измененный список."""
    for i in range(len(nums)):
        if nums[i] < 0:
            del nums[i]

    return nums

# import random
#
# n = 10
# nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
# print(nums)
#
# non_negatives(nums)
# print(nums)


"""
Ошибки (номера строк через пробел, данная строка - №2): 7
"""


def non_negatives(nums):
    """Удалить из списка чисел 'nums' отрицательные элементы и вернуть
    измененный список."""
    i = 0
    while i < len(nums):
        if nums[i] < 0:
            del nums[i]
        else:
            i += 1

    return nums