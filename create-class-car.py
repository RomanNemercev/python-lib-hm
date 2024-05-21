# %%writefile car.py
class Car(object):
    # Наименование класса
    Name_class = 'Автомобиль'

    def __init__ (self, brand, weight, power):
        self.brand = brand
        self.weight = weight
        self.power = power

    # метод двигаться прямо
    def drive(self):
        # здесь команды двигаться прямо
        print("Машина едет прямо")

    # метод повернуть направо
    def right(self):
        # здесь команды повернуть направо
        print("Машина повернула направо")

    # метод повернуть налево
    def left(self):
        # здесь команды повернуть налево
        print("Машина повернула налево")

    # метод тормозить
    def brake(self):
        # здесь команды тормозить
        print("Машина тормозит")

    # метод открыть машину
    def open(self):
        # здесь команды открыть машину
        print("Машина открыта")

    # метод закрыть машину
    def close(self):
        # здесь команды закрыть машину
        print("Машина остановилась")

    # метод подать звуковой сигнал
    def beep(self):
        # здесь команды подать звуковой сигнал
        print("Машина подала звуковой сигнал")

# from car import Car

myCar = Car('Toyota', 1000, 100)

print('Параметры автомобиля, созданного из класса: ', myCar.Name_class)
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