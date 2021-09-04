"""
Hierarchical Inheritance
"""
import math
class CarClass:
    """
    Parent class for all derived classes
    """
    def __init__(self):
        """
        Initialising all datamembers of parent class
        """
        self.name = None
        self.brand = None
        self.fuel = None
        self.body = None
        self.price = None
        self.fastag = None
        self.newprice = None

    def display(self):
        """
        Display all data members which includes car name, brand, fuel, body, price
        """
        print("Car Name       : ", self.name)
        print("Brand Name     : ", self.brand)
        print("Fuel type      : ", self.fuel)
        print("Body type      : ", self.body)
        print("On-Road price  : ₹", self.price)

    def pricebreakup(self):
        """
        Price Breakup
        """
        self.fastag = 500
        self.newprice = self.price-self.fastag
        print("Ex-Showroom Price   :  ₹ {:,.2f}".format(math.trunc(0.86*self.newprice)))
        print("RTO                 :  ₹ {:,.2f}".format(math.trunc(0.095*self.newprice)))
        print("Insurance           :  ₹ {:,.2f}".format(math.trunc(0.045*self.newprice)))
        print("Fastag              :  ₹ {:,.2f}".format(self.fastag))
        print("Total               :  ₹ {:,.2f}".format(self.price))

#TATA
class Altroz(CarClass):
    """
    Derived class : Altroz
    """
    def __init__(self):
        """
        Initialising data members
        """
        super().__init__
        self.name = "Altroz"
        self.brand = "TATA"
        self.fuel = "Petrol"
        self.body = "Hatchback"
        self.price = 904590

class Harrier(CarClass):
    """
    Derived class : Harrier
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Harrier"
        self.brand = "TATA"
        self.fuel = "Diesel"
        self.body = "SUV"
        self.price = 1738293

class Nexon(CarClass):
    """
    Derived class : Nexon
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Nexon"
        self.fuel = "Electric "
        self.brand = "TATA"
        self.body = "Compact SUV"
        self.price = 1820500

#Maruti Suzuki
class Swift(CarClass):
    """
    Derived class : Swift
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Swift"
        self.fuel = "Petrol"
        self.brand = "Maruti Suzuki"
        self.body = "Hatchback"
        self.price = 819540

class Vitara(CarClass):
    """
    Derived class : Vitara
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Vitara Breeza"
        self.fuel = "Diesel"
        self.brand = "Maruti Suzuki"
        self.body = "Compact SUV"
        self.price = 1142500

class Ciaz(CarClass):
    """
    Derived class : Ciaz
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Ciaz"
        self.fuel = "Petrol"
        self.brand = "Maruti Suzuki"
        self.body = "Sedan"
        self.price = 1324500

#Skoda
class Rapid(CarClass):
    """
    Derived class : Rapid
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Rapid"
        self.fuel = "Petrol"
        self.brand = "Skoda"
        self.body = "Sedan"
        self.price = 1256700

class Superb(CarClass):
    """
    Derived class : Superb
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Superb"
        self.fuel = "Petrol"
        self.brand = "Skoda"
        self.body = "Sedan"
        self.price = 3858900

class Octavia(CarClass):
    """
    Derived class : Octavia
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Octavia"
        self.fuel = "Petrol"
        self.brand = "Skoda"
        self.body = "Sedan"
        self.price = 3130200

#Honda
class Jazz(CarClass):
    """
    Derived class : Jazz
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Jazz"
        self.fuel = "Petrol"
        self.brand = "Honda"
        self.body = "Sedan"
        self.price = 901600

class City(CarClass):
    """
    Derived class : City
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "City"
        self.fuel = "Diesel"
        self.brand = "Honda"
        self.body = "Sedan"
        self.price = 1553600

class Wrv(CarClass):
    """
    Derived class : WR-V
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Octavia"
        self.fuel = "Petrol"
        self.brand = "Honda"
        self.body = "Compact SUV"
        self.price = 1158900

#Hyundai
class I20(CarClass):
    """
    Derived class : I20
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "I20"
        self.fuel = "Petrol"
        self.brand = "Hyundai"
        self.body = "Hatchback"
        self.price = 988450

class Creta(CarClass):
    """
    Derived class : Creta
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Creta"
        self.fuel = "Diesel"
        self.brand = "Hyundai"
        self.body = "SUV"
        self.price = 1653900

class Verna(CarClass):
    """
    Derived class : Verna
    """
    def __init__(self):
        """
        Initialising data members
        """
        self.name = "Verna"
        self.fuel = "Petrol"
        self.brand = "Hyundai"
        self.body = "Sedan"
        self.price = 1458050
