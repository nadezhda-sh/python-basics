# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func():
    alp_lat = set(chr(i) for i in range(ord('a'), ord('z') + 1))
    string_lower = input('Введите строку из слов через пробел: ').lower().split( )
    for word in string_lower:
        for let in word.split():
            if len(set(let[1:]).intersection(alp_lat)) > 0:
                string = ' '.join(string_lower)
                return string.title()
            else:
                return 'Attention: Используем только латинские буквы'



print(int_func())
