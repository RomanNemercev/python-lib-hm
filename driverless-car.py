# %%writefile driverless-car.py

class Car:
    def __init__(self, brand, weight, power):
        self.brand = brand
        self.weight = weight
        self.power = power

    def drive(self):
        print("Машина едет прямо")

    def right(self):
        print("Машина повернула направо")

    def left(self):
        print("Машина повернула налево")

    def brake(self):
        print("Машина тормозит")

    def open(self):
        print("Машина открыта")

    def close(self):
        print("Машина закрыта")

    def beep(self):
        print("Машина подала звуковой сигнал")


# from driverless-car import Car

myCar = Car('Toyota', 1000, 100)

print('Параметры автомобиля, созданного из класса: ', myCar.brand)
print('Марка (модель) - ', myCar.brand)
print('Вес (кг) - ', myCar.weight)
print('Мощность (л.с.) - ', myCar.power)

myCar.drive()
myCar.right()
myCar.left()
myCar.brake()
myCar.open()
myCar.close()
myCar.beep()