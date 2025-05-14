#Реализуйте рекурсивный алгоритм вычисления произведения суммы списка.
def recursive_sum(x):
    if not x:
        return 0
    return x[0] + recursive_sum(x[1:])

numbers = [2, 3, 4, 5]
result = recursive_sum(numbers)
print(result)  

# Сложность алгоритма: O(n^2)
