# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func():
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    c = float(input('Введите третье число: '))
    my_list = [a, b, c]
    my_list.remove(min(a, b, c))
    summa = sum(my_list)
    return summa


res = my_func()
print(f"Сумма: {res}")
