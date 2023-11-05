class Transport:
    name = "NULL"
    def __init__(self, time, money, distance, city1, city2):
        self.time = time
        self.money = money
        self.distance = distance
        self.city1 = city1
        self.city2 = city2
    def travel(self):
        pass

class Plane(Transport):
    def travel(self):
        self.name = "Самолет"

class Train(Transport):
    def travel(self):
        self.name = "Поезд"

class Car(Transport):
    def travel(self):
        self.name = "Машина"

if __name__ == '__main__':
    plane = {"time": 1.10, "money": 285, "distance": 675, "city1": "Минск", "city2": "Москва"}
    train = {"time": 6.24, "money": 122, "distance": 675, "city1": "Минск", "city2": "Москва"}
    car = {"time": 9.32, "money": 100, "distance": 675, "city1": "Минск", "city2": "Москва"}
    workPlane = Plane(**plane)
    workPlane.travel()
    workTrain = Train(**train)
    workTrain.travel()
    workCar = Car(**car)
    workCar.travel()
    vehicles = [workPlane, workTrain, workCar]
    best_time = float('inf')
    best_cost = float('inf')
    best_vehicle = None
    for vehicle in vehicles:
        if vehicle.time < best_time or (vehicle.time == best_time and vehicle.money < best_cost):
            best_time = vehicle.time
            best_cost = vehicle.money
            best_vehicle = vehicle
print(f"Наиболее быстрая и экономичная поездка: {best_vehicle.name} - Время: {best_time} часов, Стоимость: {best_cost} рублей")
with open("Транспор.txt", "a", encoding="utf-8") as FILE:
    FILE.write(f"Наиболее быстрая и экономичная поездка: {best_vehicle.name} - Время: {best_time} часов, Стоимость: {best_cost} рублей\n")
