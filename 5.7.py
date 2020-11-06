# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

profit = {}
total_profit = 0
quantity = 0
with open('task_5.7.txt') as f_obj:
    content = f_obj.readlines()
    for line in content:
        name, owner, proceed, cost = line.split()
        profit[name] = int(proceed) - int(cost)
        if profit.setdefault(name) > 0:
            total_profit += profit.setdefault(name)
            quantity += 1
    average = total_profit / quantity
    average_profit = {'Средняя прибыль': average}
res_list = (profit, average_profit)
print(res_list)
with open('task_5.7.json', 'w') as file:
    json.dump(res_list, file)
