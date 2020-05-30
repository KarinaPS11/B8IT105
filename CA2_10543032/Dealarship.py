
"""
Student Name:       Karina Jonina 
Student ID:         10543032
Github:             https://github.com/KarinaPS11/B8IT105
Module:             B8IT105 
Module Name:        Programming for Big Data (DBS)

Assignment 2        10% Car Rental Application
"""

from car import *

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.hybrid_cars = []
        self.diesel_cars = []


    def create_current_stock(self):
        for i in range(6):
           self.electric_cars.append(ElectricCar())
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())
        for i in range(10):
           self.diesel_cars.append(DieselCar())

    def stock_count(self):
        print('Our Car Stock')
        # each list of cars contains Car objects. The len of the list give us the number of cars
        print('Petrol cars in stock: ' + str(len(self.petrol_cars)))
        print('Electric cars in stock: ' + str(len(self.electric_cars)))
        print('Diesel Cars in stock: ' + str(len(self.diesel_cars)))
        print('Hybrid cars in stock: ' + str(len(self.hybrid_cars)))
        

    def rent_car(self, car_list, amount, type_car, answ):
        # Checking whether there is enough stock
        if len(car_list) < amount and len(car_list) > 0:
            print('The stock is not enough.')

        elif len(car_list) > amount or len(car_list) == amount:
            total = 0
            while total < amount:
                car_list.pop()
                total = total + 1
           
    def return_car(self, car_list, amount):
        total = 0
        while total < amount:
            car_list.append(1)
            total = total + 1

    def process_hire(self):
        # the user can choose to rent or return a car
        answer = input('Would you like to hire a car H, return a car R, any key to quit?\n')
        print(self.stock_count())

        #if hire is chosen:
        if answer == 'H':
            answ = ''
            type_car = input('What car would you like to rent - P for petrol, E for electric, D for diesel, H for hybrid?\n')
            amount = int(input('How many would you like renting?\n'))
            if type_car == 'P':
                self.rent_car(self.petrol_cars, amount, type_car, answ)
            elif type_car == 'E':
                self.rent_car(self.electric_cars, amount, type_car, answ)
            elif type_car == 'D':
                self.rent_car(self.diesel_cars, amount, type_car, answ)
            elif type_car == 'H':
                self.rent_car(self.hybrid_cars, amount, type_car, answ)
            return self.stock_count()
        
        #if return is chosen
        elif answer == 'R':
            type_car = input('What car would you like to return - P for petrol, E for electric, D for diesel, H for hybrid?\n')
            amount = int(input('How many would you like returning?\n'))
            if type_car == 'P':
                self.return_car(self.petrol_cars, amount)
            elif type_car == 'E':
                self.return_car(self.electric_cars, amount)
            elif type_car == 'D':
                self.return_car(self.diesel_cars, amount)
            elif type_car == 'H':
                self.return_car(self.hybrid_cars, amount)
            return self.stock_count()
        
    # Save stock  
    def save_csv(self):   
        csv_file = open('cars.csv', 'w')
        csv_file.write('Type, Stock\n')
        csv_file.write('P,' + str(len(self.petrol_cars)) + '\n')
        csv_file.write('E, ' + str(len(self.electric_cars)) + '\n')
        csv_file.write('D, ' + str(len(self.diesel_cars)) + '\n')
        csv_file.write('H, ' + str(len(self.hybrid_cars)) + '\n')
        csv_file.close()
     
if __name__ == '__main__':
    dealership = Dealership()
    dealership.create_current_stock()
    proceed = 'y'
    while proceed == 'y':
        dealership.process_hire()
        proceed = input('Would you like to continue? y/n')
    dealership.save_csv()