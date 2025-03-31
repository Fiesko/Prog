

# Задание task_03_01_02.
#
# Выполнил: Малеванный И.Б
# Группа: ЦИБ - 241



def avg(data):
  data = round(sum(cleared_data(data))/len(cleared_data(data)),2)
  return data


def cleared_data(data):
    while None in data:
      data.remove(None)
    else:
      return data


n = int(input('Кол-во измерений: '))

# Если с клавиатуры вводится прочерк, измерения нет
# (необходимо добавить в список None)
data = list()
c = 1
for i in range(n):
  a = input(f'Измерение {c}-e: ')
  c+=1
  if a == '-':
    data.append(None)
  else:
    data.append(int(a))



# Получить очищенный список и среднее значение

print('Средняя температура:', avg(data))
# --------------
# Пример вывода:
#
# Кол-во измерений: 3
# Измерение 1-е: 10
# Измерение 2-е: -
# Измерение 3-е: 20
# Средняя температура: 15.00
