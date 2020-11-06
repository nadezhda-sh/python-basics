# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
new_list = []
with open('task_5.4_origin.txt', 'r') as f_obj:
    with open('task_5.4_finish.txt', 'w') as out:
        content = f_obj.readlines()
        for line in content:
            line = line.strip().split('\n')
            for el in line:
                el = el.replace('One', 'Один')
                el = el.replace('Two', 'Два')
                el = el.replace('Three', 'Три')
                el = el.replace('Four', 'Четыре')
                new_list.append(el)
        out.write('\n'.join(new_list))
