"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            if self.__color[0] == 'red' \
                    and self.__color[1] == 'yellow' \
                    and self.__color[2] == 'green':
                print(self.__color[0])
                sleep(7)
                print(self.__color[1])
                sleep(2)
                print(self.__color[2])
                sleep(10)
            else:
                print('Error!')
                break


traffic_light = TrafficLight(['red', 'yellow', 'green'])
traffic_light.running()

