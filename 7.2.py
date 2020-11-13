# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class AbstractClothes(ABC):

    @abstractmethod
    def textile(self):
        pass


class Coat(AbstractClothes):

    def __init__(self, size):
        self._size = size

    @property
    def textile(self):
        return self._size / 6.5 + 0.5


class Costume(AbstractClothes):

    def __init__(self, height):
        self._height = height

    @property
    def textile(self):
        return 2 * self._height + 0.3


coat = Coat(float(input('Введите размер пальто: ')))
print('%.2f' % coat.textile)

costume = Costume(float(input('Введите рост для костюма в метрах: ')))
print('%.2f' % costume.textile)
