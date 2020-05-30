"""
Student Name:       Karina Jonina 
Student ID:         10543032
Github:             https://github.com/KarinaPS11/B8IT105
Module:             B8IT105 
Module Name:        Programming for Big Data (DBS)

Assignment 2        10% Car Rental Application
"""

import unittest
from Dealarship import *
import csv
import os.path

class Test_Dealership(unittest.TestCase):
    
    def setUp(self):
        self.deal = Dealership()
        
        #creating stock to test
        self.deal.create_current_stock()


    def test_process_hire(self):
        self.assertTrue(self.deal.process_hire)
        
    #check if save complete 
    def test_curerent_file(self): 
        self.assertTrue(os.path.isfile('cars.csv'))
    

    
if __name__ == "__main__":
    unittest.main()      