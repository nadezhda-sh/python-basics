# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):

    def draw(self):
        return f'Паста закончилась'


class Pencil(Stationery):

    def draw(self):
        return f'Линия бледна'


class Handle(Stationery):

    def draw(self):
        return f'Жирненькая линия'


big = Pen('Ручка Big')
const = Pencil('Карандаш Консруктор')
copic = Handle('Маркер COPIC')
print(f'{big.title}: {big.draw()}')
print(f'{const.title}: {const.draw()}')
print(f'{copic.title}: {copic.draw()}')
