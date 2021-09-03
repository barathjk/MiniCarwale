import math
class carclass:
    def __init__(self):
        self.name = None
        self.brand = None
        self.fuel = None
        self.body = None
        self.price = None

    def display(self):
        print("Car Name       : ", self.name)
        print("Brand Name     : ", self.brand)
        print("Fuel type      : ", self.fuel)
        print("Body type      : ", self.body)
        print("On-Road price  : ₹", self.price) 
    
    def pricebreakup(self):
        self.fastag = 500
        self.newprice = self.price-self.fastag
        print("Ex-Showroom Price   :  ₹ {:,.2f}".format(math.trunc(0.86*self.newprice)))
        print("RTO                 :  ₹ {:,.2f}".format(math.trunc(0.095*self.newprice)))
        print("Insurance           :  ₹ {:,.2f}".format(math.trunc(0.045*self.newprice)))
        print("Fastag              :  ₹ {:,.2f}".format(self.fastag))
        print("Total               :  ₹ {:,.2f}".format(self.price))

#TATA
class altroz(carclass):
    def __init__(self):
        self.name = "Altroz"
        self.brand = "TATA"
        self.fuel = "Petrol"
        self.body = "Hatchback"
        self.price = 904590

class harrier(carclass):
    def __init__(self):
        self.name = "Harrier"
        self.brand = "TATA"
        self.fuel = "Diesel"
        self.body = "SUV"
        self.price = 1738293

class nexon(carclass):
    def __init__(self):
        self.name = "Nexon"
        self.fuel = "Electric "
        self.brand = "TATA"
        self.body = "Compact SUV"
        self.price = 1820500

#Maruti Suzuki
class swift(carclass):
    def __init__(self):
        self.name = "Swift"
        self.fuel = "Petrol"
        self.brand = "Maruti Suzuki"
        self.body = "Hatchback"
        self.price = 819540

class vitara(carclass):
    def __init__(self):
        self.name = "Vitara Breeza"
        self.fuel = "Diesel"
        self.brand = "Maruti Suzuki"
        self.body = "Compact SUV"
        self.price = 1142500

class ciaz(carclass):
    def __init__(self):
        self.name = "Ciaz"
        self.fuel = "Petrol"
        self.brand = "Maruti Suzuki"
        self.body = "Sedan"
        self.price = 1324500

#Skoda
class rapid(carclass):
    def __init__(self):
        self.name = "Rapid"
        self.fuel = "Petrol"
        self.brand = "Skoda"
        self.body = "Sedan"
        self.price = 1256700

class superb(carclass):
    def __init__(self):
        self.name = "Superb"
        self.fuel = "Petrol"
        self.brand = "Skoda"
        self.body = "Sedan"
        self.price = 3858900

class octavia(carclass):
    def __init__(self):
        self.name = "Octavia"
        self.fuel = "Petrol"
        self.brand = "Skoda"
        self.body = "Sedan"
        self.price = 3130200

#Honda
class jazz(carclass):
    def __init__(self):
        self.name = "Jazz"
        self.fuel = "Petrol"
        self.brand = "Honda"
        self.body = "Sedan"
        self.price = 901600

class city(carclass):
    def __init__(self):
        self.name = "City"
        self.fuel = "Diesel"
        self.brand = "Honda"
        self.body = "Sedan"
        self.price = 1553600

class wrv(carclass):
    def __init__(self):
        self.name = "Octavia"
        self.fuel = "Petrol"
        self.brand = "Honda"
        self.body = "Compact SUV"
        self.price = 1158900

#Hyundai
class i20(carclass):
    def __init__(self):
        self.name = "i20"
        self.fuel = "Petrol"
        self.brand = "Hyundai"
        self.body = "Hatchback"
        self.price = 988450

class creta(carclass):
    def __init__(self):
        self.name = "Creta"
        self.fuel = "Diesel"
        self.brand = "Hyundai"
        self.body = "SUV"
        self.price = 1653900

class verna(carclass):
    def __init__(self):
        self.name = "Verna"
        self.fuel = "Petrol"
        self.brand = "Hyundai"
        self.body = "Sedan"
        self.price = 1458050
