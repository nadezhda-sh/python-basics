# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(*args):
    if all(96 < ord(let) < 123 for let in word):
        new_string = ''.join(word)
        return new_string.title()
    else:
        return 'Не те буквы'


string = input('Введите слова: ').lower().split()
for word in string:
    res = int_func()
    print(res)
