"""
Student Name:       Karina Jonina 
Student ID:         10543032
Github:             https://github.com/KarinaPS11/B8IT105
Module:             B8IT105 
Module Name:        Programming for Big Data (DBS)

Assignment 3        10% - 10 Functional Calculator with Map Reduce Filter & Generator
"""


#for Python 3, import the important package
from functools import reduce

class Calculator(object):
    

    # FUNCTION 1  - adding with lamdbda and reduce
    def add_all_values(self, values):
        return reduce(lambda x, y: x + y, values)
    
    # FUNCTION 2  - adding with lamdbda and reduce
    def subtract_all_values(self, data):
         return reduce(lambda x, y: x - y, data)      
    
    # FUNCTION 3  - adding with lamdbda and reduce
    def divide_all_values(self, data):
        return reduce(lambda x, y: x / y, data)      

    # FUNCTION 4  - adding with lamdbda and reduce
    def multiply_all_values(self, data):
        return reduce(lambda x, y: x * y, data)

    # FUNCTION 5 - finding max values with with lamdbda and reduce
    def maximum(self, values):
        return reduce(lambda x, y: x if (x > y) else y, values) 
    
    # FUNCTION 6 - finding min values with with lamdbda and reduce
    def minimum(self, values):
        return reduce(lambda x, y: x if (x < y) else y, values) 
    
    # FUNCTION 7 -  finding adding two values with lamdbda and map
    def add_lists(self, first, second):
        return list(map(lambda x, y: x + y, first, second))
    
    # FUNCTION 8 -  finding subtracting items in two values with lamdbda and map
    def minus_lists(self, first, second):
        return list(map(lambda x, y: x - y, first, second))

    # FUNCTION 9 -  finding multiply items in two values with lamdbda and map
    def multiply_lists(self, first, second):
        return list(map(lambda x, y: x * y, first, second))
    
    # FUNCTION 10 -  finding dividing items in two values with lamdbda and map
    def divide_lists(self, first, second):
        return list(map(lambda x, y: x / y, first, second))
    
    # FUNCTION 11 - finding which which values are odd with filter
    def is_odd(self, values):
        return list(filter(lambda x: x % 2, values))
    
    # FUNCTION 12 - finding which which values are even with filter
    def is_even(self, values):
        return list(filter(lambda x: x % 2 == 0, values))
    
    # FUNCTION 13 - finding which value(s) is (are) greater than the mean with filter
    def greater_than_mean(self, values):
        mean = sum(values)/len(values)
        return list(filter(lambda x: x > mean, values))
    
    # FUNCTION 14 - generating sums of squares
    def generator_square(self, values):
        for i in values:
            yield(i * i)
#    
    # FUNCTION 15 - fibonacci
    def fibonacci(n):
        """ A generator for creating the Fibonacci numbers """
        a, b, counter = 0, 1, 0
        while True:
            if (counter > n): 
                return
            yield a
            a, b = b, a + b
            counter += 1

    # FUNCTION 16 - pythageos triplets using comprehension
    def pythageos(self):
        max_values = int(input('What number would you like the pythageos to go up to? '))
        return [(x,y,z) for x in range(1,max_values) for y in range(x,max_values) for z in range(y, max_values) if x**2 + y**2 == z**2]

    #FUNCTION 17 - changing Kilometres to Miles using comprehension
    def toKM(self, values):
        return [ ((float(x) / 5) * 8) for x in values ]
    
    #FUNCTION 18 - changing Kilometres to Miles using comprehension
    def toMiles(self, values):
        return [ ((float(x) / 8) * 5) for x in values ]



    def operator_menu(self):
        print('1 to do addition of the whole set')
        print('2 to do subtract of the whole set')
        print('3 to do multiplication of the whole set')
        print('4 to do division of the whole set')        
        print('5 to find maximum in the set')
        print('6 to find minimum in the set')
        print('7 to add two sets together')
        print('8 to subtract two sets from each other')
        print('9 to multiply two sets together')
        print('10 to divide two sets')
        print('11 to find odd numbers in the set')
        print('12 to find even numbers in the set')        
        print('13 to find which number is greater than mean in the set')
        print('14 to generate sums of squares')
        print('15 to create a fibonacci')
        print('16 to create a pythageos triples')
        print('17 to convert Miles to Kilometres')
        print('18 to covert Kilometres to Miles')
    
    def process_operation(self):

        Calculator().operator_menu()
        items = list(map(float, input('Please write your set of numbers in (separated by commas : ').split(',')))
        func = input('Choose an operation. Here is a menu: ')
        if func not in ['1', '2', '3', '4', '5', '6', '11', '12', '13', '14', '15', '16', '17', '18']:
            items2 = list(map(float, input('Please write your second set of numbers in (separated by commas : ').split(',')))
        

       
        if func in ['1']:
            print('Total of all numbers in the set is: ', Calculator().add_all_values(items))
        if func in ['2']:
            print('Results of subtracting of all numbers in the set is: ', Calculator().subtract_all_values(items))            
        if func in ['3']:
            print('Product of all numbers in the set is: ', Calculator().multiply_all_values(items))
        if func in ['4']:
            print('Results of division of all numbers in the set is: ', Calculator().divide_all_values(items))
        if func in ['5']:
            print('The minimum number in the set is: ', Calculator().maximum(items))
        if func in ['6']:
            print('The Mmaximum number in the set is: ',Calculator().minimum(items))
        if func in ['7']:
            print(Calculator().add_lists(items, items2))
        if func in ['8']:
            print(Calculator().minus_lists(items, items2))
        if func in ['9']:
            print(Calculator().multiply_lists(items, items2))
        if func in ['10']:
            print(Calculator().divide_lists(items, items2))
        if func in ['11']:
            print('The odd numbers in the set are: ', Calculator().is_odd(items))
        if func in ['12']:
            print('The even numbers in the set are: ', Calculator().is_even(items))
        if func in ['13']:
            print('The numbers greatere than the mean in the set is: ',Calculator().greater_than_mean(items))
        if func in ['14']:
            print(list(Calculator().generator_square(items)))
        if func in ['15']:
            print(list(Calculator().fibonacci()))
        if func in ['16']:
            print('The pythageos triplets to your chosen number is: ', Calculator().pythageos())
        if func in ['17']:
            print('The conversion to Km is: ', Calculator().toKM(items))
        if func in ['18']:
            print('The conversion to Miles is: ', Calculator().toMiles(items))

   
    def process(self):
        ask_again = ''
        while ask_again != 'y':
            Calculator().process_operation()
            ask_again = input('Would you like to exit the calculator (y/n)? ')

if __name__ == '__main__':
    Calculator().process()


#to use the generator correctly
x = Calculator().generator_square(items)
print(next(x))
