class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname} – {self.position}"

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]

if __name__ == '__main__':
    worker = {"name": "Егор", "surname": "Никитин", "position": "back-end разработчик", "income": {"wage": 2500, "bonus": 1000}}
    position = Position(**worker)
    print(f"Имя и Фамилия и должность: {position.get_full_name()}")
    print(f"Доход с учетом премии: {position.get_total_income()}")