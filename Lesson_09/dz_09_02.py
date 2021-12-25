class Road:

    _length = 0
    _width = 0

    def __init__(self):
        Road._length = int(input('Введите длину: '))
        Road._width = int(input('Введите ширину: '))

    def asphalt_mass(self, depth=5):
        """ Можно указать толщину асфальта в см """
        wt = Road._length * Road._width * 25 * depth
        print(f'{Road._length}м * {Road._width}м * 25кг * {depth}см = {int(wt/1000)} т.')


asphalt_mark1 = Road()
asphalt_mark1.asphalt_mass()
