# -*- coding: utf-8 -*-
"""
Student Name:       Karina Jonina 
Student ID:         10543032
Github:             https://github.com/KarinaPS11/B8IT105
Module:             B8IT105 
Module Name:        Programming for Big Data (DBS)

Assignment 1        10% - Beautiful Soup
"""

import unittest

import corona_London_website

class TestCorona(unittest.TestCase):
    
    def setUp(self):
        self.contents = corona_London_website.get_page_contents()
         
              
    def test_get_page_contents(self):
        self.assertTrue(len(self.contents) > 0)
        
        
    def test_convert_To_soup(self):
        self.assertTrue(corona_London_website.convert_to_soup(self.contents) is not None)
        
#    def test_find_all_links(self):
#        soup =  corona_London_website.convert_to_soup(self.contents)
#        self.assertTrue(len(corona_London_website.find_all_links(soup)) > 50)


if __name__ == '__main__':
    unittest.main()    