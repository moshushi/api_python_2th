class Vehicle:
    __engine_status = "Off"

    def __init__(self, brand, model, wheels):
        self.brand = brand
        self.model = model
        self._wheels = wheels

    def set_engine_status(self, status):
        if status not in ["On", "Off"]:
            print("wrong value")
        self.__engine_status = status
        # else:
        #     pass

    def get_engine_status(self):
        return  self.__engine_status

    def get_name(self):
        return f"{self.brand} {self.model}"


class LuxVehicle(Vehicle):

    # def get_name(self):
    #     raise NotImplemented("This method is not implemented!")
    def get_name(self):
        return f"!!!{self.brand} {self.model}!!!"

    def show_off(self):
        print(f"Hey you, checkout my {self.get_name()}!")

# veh = Vehicle("Toyota", "Camry", 4)
# print(veh.get_engine_status())
# veh.set_engine_status("Test")
# veh.set_engine_status("On")

v = Vehicle("Toyota", "Camry", 4)
lv = LuxVehicle("Bugatti", "Veyron", 4)

print(v.get_engine_status())
print(lv.get_engine_status())
print(isinstance(lv, Vehicle))
# print(lv.show_off())
lv.show_off()