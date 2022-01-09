import random


class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        direction = random.choice(('налево', 'направо'))
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена!')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена!')
        else:
            super().show_speed()


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


car_01 = TownCar(50, 'Yellow', 'Duster')
car_01.go()
car_01.show_speed()
car_01.speed = 100
car_01.show_speed()
car_01.turn()
car_01.stop()
print()

car_02 = SportCar(80, 'Red', 'Shark')
car_02.go()
car_02.show_speed()
car_02.turn()
car_02.stop()
print()

car_03 = WorkCar(20, 'Green', 'Bull')
car_03.go()
car_03.show_speed()
car_03.turn()
car_03.stop()
print()

car_04 = PoliceCar(100, 'Black', 'Rhino')
car_04.go()
car_04.show_speed()
car_04.turn()
car_04.stop()
print()
