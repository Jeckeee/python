"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'начинает движение'

    def stop(self):
        return 'останавливается'

    def turn(self, direction):
        return f'повернул {direction}'

    def show_speed(self):
        return f'{self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} км/ч. Превышение скорости'
        else:
            return f'{self.speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} км/ч. Превышение скорости'
        else:
            return f'{self.speed} км/ч'


class PoliceCar(Car):
    pass


mercedes = Car(80, 'Black', 'Mercedes', False)
lexus = TownCar(40, 'White', 'Lexus', False)
bmw = SportCar(160, 'Red', 'BMW', False)
audi = WorkCar(60, 'Black', 'Audi', False)
ford = PoliceCar(70, 'Black and White', 'Ford', True)

print(f'{mercedes.name} цвета {mercedes.color} {mercedes.stop()}')
print(f'{lexus.name} {lexus.go()} и {lexus.turn("направо")}')
print(f'{bmw.name} едет со скоростью {bmw.show_speed()}')
print(f'{audi.name} имеет скорость {audi.show_speed()}')
print(f'{ford.color} {ford.name} полицейский автомобиль? {ford.is_police}')
