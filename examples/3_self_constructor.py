class Car:
    engine_status = "Off"

    def __init__(self, brand, model, wheels, key):
        """Class constructor"""
        self.brand = brand
        self.model = model
        self.wheels = wheels
        self.key = key

    def start_engine(self, key):
        if key == self.key:
            self.engine_status = "On"
            print(f"Engine of {self.brand} {self.model} started. On {self.wheels} wheels.")

    def drive(self):
        if self.engine_status == "On":
            print(f"Ride on {self.brand} {self.model} started. On {self.wheels} wheels.")


    def stop_engine(self):
        if self.engine_status == "Off":
            return None
        self.engine_status = "Off"
        print(f"Engine of {self.brand} {self.model} stopped.")


# toyota_camry = Car(brand="Toyota", model="Canryself", wheels=4)
# honda_trio = Car(brand="Honda", model="Civic", wheels=3)