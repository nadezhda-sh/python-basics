# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, w_name, w_surname, w_position, wage, bonus):
        self.name = w_name
        self.surname = w_surname
        self.position = w_position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя: {self.name + " " + self.surname}')

    def get_total_income(self):
        print(f'Сумма дохода: {sum(self._income.values())}')


pers = Position(w_name=input('Введите имя: '), w_surname=input('Введите фамилию: '),
                w_position=input('Введите должность: '), wage=float(input('Введите оклад сотрудника: ')),
                bonus=float(input('Введите премию сотрудника: ')))
pers.get_full_name()
print(f'Должность: {pers.position}')
pers.get_total_income()
