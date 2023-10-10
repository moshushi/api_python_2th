class Car:
    WHEELS = 4
    def drive(self):
        print("Car is driving")
    def stop(self):
        print("Car stopped")

car = Car()

print(car.WHEELS)
car.stop()