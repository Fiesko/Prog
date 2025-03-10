# Задание task_02_34.
#
# Выполнил: Малеванный И.Б.
# Группа: ЦИБ-241



# 1. Заполнение списка

# Используйте данный список для собственных тестов,
# чтобы избежать постоянного ввода значений
# Перед автоматической проверкой удалите его
# и используйте ввод с клавиатуры

n = int(input("Количество банков: "))

deposits = []
for i in range(n):
    bank_info = input(f"Введите данные для банка {i + 1} (Банк Сумма Процент): ").split()
    name = bank_info[0]
    initial_sum = int(bank_info[1])
    rate = float(bank_info[2])
    deposits.append({"name": name, "initial_sum": initial_sum, "rate": rate})

# 2. Самый доступный банк (с наименьшей первоначальной суммой)

min_initial_sum_bank = min(deposits, key=lambda x: x["initial_sum"])


# 3. Самый выгодный банк
#    прибыль = сумма * процент / 100
most_profitable_bank = max(deposits, key=lambda x: x["initial_sum"] * x["rate"] / 100)

print(f"Количество банков = {n}")
for deposit in deposits:
    print(f"{deposit['name']} {deposit['initial_sum']} {deposit['rate']}")

print(f"Самый доступный банк: {min_initial_sum_bank['name']}, первоначальная сумма: {min_initial_sum_bank['initial_sum']:.2f} руб.")
print(f"Самый выгодный банк: {most_profitable_bank['name']}, прибыль: {most_profitable_bank['initial_sum'] * most_profitable_bank['rate'] / 100:.2f} руб.")
# --------------
# Пример вывода:
#
# Количество банков = 3
# Банк_1 50000 5.2
# Банк_2 20000 3.7
# Банк_3 45000 6.8
# Самый доступный банк: Банк_2, первоначальная сумма: 20000.00 руб.
# Самый выгодный банк: Банк_3, прибыль: 3060.00 руб.
