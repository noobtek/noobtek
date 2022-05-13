"""MULTIPLE INHERITANCE"""
'''Parent 1'''
class Vehicle:
    def __init__(self,color,type,price,mileage):
        self.color=color
        self.type=type
        self.price=price
        self.mileage=mileage
    def Vehicle_details(self):
        print("This is a Vehicle")
        print("The color is: ",self.color)
        print("The type is: ", self.type)
        print("The price is: ", self.price)
        print("The mileage is: ", self.mileage)
s=Vehicle("Magenta","Sedan","1500000","15")
s.Vehicle_details()

"""PARENT 2"""

class Car:
    def __init__(self,tyre,occupancy,transmission):
        self.tyre=tyre
        self.occupancy=occupancy
        self.transmission=transmission
    def Car_Details(self):
        print("Brand of Tyre is: ",self.tyre)
        print("Seating Capacity is: ",self.occupancy)
        print("The Transmission is: ",self.transmission)
s1=Car("MRF",5,"Automatic")
s1.Car_Details()
'''Child Class''' # do parent class ek child class me kaise aaenge batade yar
class Childclass(Vehicle,Car):
    def __init__(self,color,type,price,mileage,tyre,occupancy,transmission,Brand,YearofMake):
        super().__init__(color,type,price,mileage)
        super().__init__(tyre,occupancy,transmission)
        self.Brand=Brand
        self.YearofMake=YearofMake

    def childclass_car_details(self):
        print("This is a car inheriting traits from above class")
        print("Brand is: ",self.Brand)
        print("Year of Make: ",self.YearofMake)

s2=Childclass("Black","Sedan",2000000,10,"MRF",5,"Automatic" ,"Hyundai",2022)

s2.childclass_car_details()
s2.Vehicle_details()
# s2.Car_Details()