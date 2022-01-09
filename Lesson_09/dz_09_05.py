class Stationery:

    title = 'Название'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    title = 'Ручка'

    def draw(self):
        print(f'{self.title} чертит тоненькую, аккуратную линию')


class Pencil(Stationery):

    title = 'Карандаш'

    def draw(self):
        print(f'{self.title} чертит толстую стираемую линию')


class Handle(Stationery):

    title = 'Маркер'

    def draw(self):
        print(f'{self.title} чертит жирную яркую линию')


pen = Pen()
pen.draw()
print()

pencil = Pencil()
pencil.draw()
print()

handle = Handle()
handle.draw()
