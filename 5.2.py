# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('task_5.2.txt', 'r') as f_obj:
    lines = f_obj.readlines()
    print(f'Количество строк: {len(lines)}')
    for line in lines:
        print(f'Количество слов в строке: {len(line.strip().split(" "))}')
