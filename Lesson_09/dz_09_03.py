class Worker:

    name = 'Имя'
    surname = 'Фамилия'
    position = 'Должность'
    _income = {"wage": 3000, "bonus": 500}


class Position(Worker):

    def get_full_name(self):
        Worker.name = input('Введите имя сотрудника: ')
        Worker.surname = input('Введите фамилию сотрудника: ')

    def get_total_income(self):
        return Worker._income.get("wage") + Worker._income.get("bonus")


worker_001 = Position()
worker_001.get_full_name()
print(f'Сотрудник {Worker.name} {Worker.surname} в сумме получает {worker_001.get_total_income()}$')

worker_002 = Position()
worker_002.get_full_name()
print(f'Сотрудник {Worker.name} {Worker.surname} в сумме получает {worker_002.get_total_income()}$')
