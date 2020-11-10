# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import random
import time


class Car:
    def __init__(self, speed: int, color: str, name: str, police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = police
        self.go()
        self.turn()
        self.show_speed()
        self.stop()

    def go(self):
        if self.speed > 0:
            print(f'Машина {self.name} поехала')

    def stop(self):
        if self.speed == 0:
            print(f'Машина {self.name} стоит')
        else:
            time.sleep(3)
            self.speed = 0
            print(f'Машина {self.name} остановилась')

    def turn(self):
        route = ('Да, на лево', 'Да, на право', 'Нет, проехала поворот и поехала прямо')
        if self.speed > 0:
            direction = random.choice(route)
            print(f'{self.name} повернула?')
            time.sleep(2)
            print(direction)

    def show_speed(self):
        print(f'Скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости! Скорость {self.speed}, разрешенная 60')
        else:
            print(f'Скорость: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости! Скорость {self.speed}, разрешенная 40')
        else:
            print(f'Скорость: {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, police: bool):
        super().__init__(speed, color, name, police)
        self.is_police = True
        print(f'Машина {self.name} - полицеская машина!')


vaz = TownCar(50, 'черный', 'ВАЗ', False)
print('\n')
gazel = TownCar(65, 'белая', 'Газель', False)
print('\n')
zhiguli = SportCar(0, 'красная', 'Жигули', False)
print('\n')
ford = WorkCar(47, 'зеленый', 'Форд', False)
print('\n')
lada = PoliceCar(80, 'комбинированный цвет', 'Лада', True)
