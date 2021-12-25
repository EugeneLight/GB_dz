from time import sleep


class TrafficLight:

    __color = 'красный'
    start = 'красный'

    def __init__(self):
        print(TrafficLight.__color)

    def running(self, loop=1):
        for n in range(loop * 3):
            if TrafficLight.__color == 'красный' or TrafficLight.__color == 'зелёный':
                sleep(7)
                TrafficLight.__color = 'жёлтый'
            elif TrafficLight.__color == 'жёлтый':
                sleep(2)
                if TrafficLight.start == 'красный':
                    TrafficLight.__color = 'зелёный'
                elif TrafficLight.start == 'зелёный':
                    TrafficLight.__color = 'красный'
                TrafficLight.start = TrafficLight.__color
            print(TrafficLight.__color)


light = TrafficLight()
light.running()
