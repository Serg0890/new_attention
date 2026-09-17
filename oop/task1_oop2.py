class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self) -> str:
        return self.model


class Truck(Car):

    def __init__(self, trunk_fullness=0, model="грузовой авто"):
        super().__init__(model)
        self.trunk_fullness = trunk_fullness

    def loading(self):
        self.trunk_fullness = 100
        print(f"{self} заполнен")

    def uploading(self):
        self.trunk_fullness = 0
        print(f"{self} заполнен")


class PassCar(Car):
    def __init__(self, gps_sys, model="легковой"):
        super().__init__(model)
        self.gps_sys = gps_sys

    def on_gps(self):
        print(f"on {self.gps_sys}")

    def of_gps(self):
        print(f"off {self.gps_sys}")


car1 = Truck()
car1.loading()
car2 = PassCar("gps")
car2.on_gps()

car2.of_gps()
