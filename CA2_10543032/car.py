

"""
Student Name:       Karina Jonina 
Student ID:         10543032
Github:             https://github.com/KarinaPS11/B8IT105
Module:             B8IT105 
Module Name:        Programming for Big Data (DBS)

Assignment 2        10% Car Rental Application
"""

import pandas as pd

class Car(object):
    carlist = []
    n = 0

    def __init__(self, make = '', model = '', types = '', colour = '', reg = '',  
                 mileage = 0, available = '', distance = ''):
        self.__make = make
        self.__model = model
        self.__type = types
        self.__colour = colour
        self.__reg = reg
        self.__mileage = mileage
        self.__available = available
        self.distance = distance

#Get Methods.
    def getMake(self):
        return self.__make
		
    def getModel(self):
        return self.__model
		
    def getType(self):
        return self.__type

    def getColour(self):
        return self.__colour

    def getReg(self):
        return self.__reg
		
    def getMileage(self):
        return self.__mileage
		
    def getAvailability(self):
        return self.__available

#Set Methods.
		
    def setMake(self, make):
        self.__make = make
	
    def setModel(self, model):
        self.__model = model	
		
    def setType(self, types):
        self.__type = types
	
    def setColour(self, colour):
        self.__colour = colour
		
    def setReg(self, reg):
        self.__reg = reg

    def setMileage(self, mileage):
        self.__mileage = mileage
		
    def setAvailability(self, available):
        self.__available = available
    
    
    def create_car(self):
        print('Enter Car Details. You can enter single numbers into all the questions')
        print('Please note: The only important variable that you must enter correctly is TYPE')
        print('Please write in P/ H/ D/ E')
        self.setMake(input("Enter Make : "))
        self.setModel(input("Enter Model : "))
        self.setType(input("Enter Type: "))
        self.setColour(input("Enter Colour : "))
        self.setReg(input("Enter Registration : "))
        self.setMileage(input("Enter Mileage : "))
        self.setAvailability(input("Enter Availability : "))

        
    def DisplayData(self):
        print('Make : ', self.getMake)
        print('Model : ', self.getModel)
        print('Type : ', self.getType)
        print('Colour : ', self.getColour)
        print('Reg : ', self.getReg)
        print('Mileage : ', self.getMileage)
        print('Availability : ', self.getAvailability)
        
    def move(self, distance):
        self.distance = int(input('Enter Distance: '))
        self.mileage = self.mileage + self.distance
        return self.mileage
    


    def create_stock(self):
        self.n = int(input('How many cars would you like to make? '))
        for i in range(self.n):
            car = Car()
            car.create_car()
            self.carlist.append(car)

#    def asDictionary(self):
#        return {'Make': self.__make, 'Model': self.__model, 'Type': self.__type,
#                'Colour': self.__colour, 'Reg': self.__reg, 'Mileage': self.__mileage,
#                'Availability': self.__available}

    def asDictionary(self):
        return {'Make': self.getMake, 'Model': self.getModel, 'Type': self.getType,
                'Colour': self.getColour, 'Reg': self.getReg, 'Mileage': self.getMileage,
                'Availability': self.getAvailability}
    dicts=[]
    def create_panda(self):
        self.create_stock()
        
        for car in self.carlist:
            self.dicts.append(self.asDictionary())


#        #creating columns for the dataset
#        car_columns = ['Make', 'Model', 'Type', 'Colour', 'Reg', 'Mileage', 'Availability']

        # creating a panda dataset for the car dealership
        car_dealership = pd.DataFrame(index = range(0, self.n), data = self.dicts)
        print(car_dealership)
        
        car_dealership.to_csv('car_dealership.csv')
        
class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

#create a petrol car (subclass)
class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

        
# create a diesel car (subclass)
class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

# create a hybrid car (subclass)
class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1
        



Car().create_panda()

