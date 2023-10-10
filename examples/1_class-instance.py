# New class declaration
class Car:
    pass

class A(Car):
    pass

car = Car()
a = A()

# Объекты класса делаются как вызов метода от данного класса
car = Car()
# car1 = Car()

# print(car)
# print(Car)

print(isinstance(car, A))


