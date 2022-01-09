class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        total = sum(self._income.values())
        return total


worker_001 = Position('Василий', 'Бровкин', 'Электрик', 6000, 400)
print(worker_001.get_full_name())
print(worker_001.get_total_income())
print()

worker_002 = Position('Пётр', 'Манечкин', 'Менеджер', 2000, 100)
print(worker_002.get_full_name())
print(worker_002.get_total_income())
