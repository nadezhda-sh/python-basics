# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
salary = []
surname = []
with open('task_5.3.txt', 'r') as f_obj:
    content = f_obj.readlines()
    for line in content:
        report = line.split()
        if float(report[1]) < 20000:
            surname.append(report[0])
        salary.append(float(report[1]))
    print(f'Сотрудники с окладом ниже 20000:\n {surname}')
    print(f'Средний доход сотрудников:\n {sum(salary)/len(salary)}')
