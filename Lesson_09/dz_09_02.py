class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, depth=5):
        wt = self._length * self._width * 25 * depth
        return f'{self._length}м * {self._width}м * 25кг * {depth}см = {int(wt/1000)} т.'


asphalt_mark1 = Road(20000, 20)
print(asphalt_mark1.asphalt_mass())
