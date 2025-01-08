import math as m
from math import sqrt, tan
class Car: 
    
    def __init__(self, brand: str, fuel_type: str) -> None:
        self.brand = brand
        self.fuel_type = fuel_type

    def drive(self, distance: float) -> None:
        print(f'Driving {self.brand} for {distance}km [{self.fuel_type}]')    

    @staticmethod
    def test() -> None:
        print("Testing.........................")   

    def test1(self, gsr: str) -> None:
        print("Testing........................." + gsr)        


volvo: Car = Car(brand = "Volvo", fuel_type = "petrol")   
Bmw: Car = Car(brand = "Bmw", fuel_type = "Electric")    
print(volvo.brand + "-" + volvo.fuel_type)
print(Bmw.brand + "-" + Bmw.fuel_type)
print("--------------------------")
volvo.drive(10)
volvo.test1(gsr="Surendar")
Bmw.drive(20)
Car.test()
print(sqrt(4))
print(tan(2))
