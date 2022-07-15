#!/usr/bin/env python3
'''TReich | Alta3 Research
    Defining custom classes'''

# Create blueprint for class Cat
class Cat:
    def __init__(self, name):
        # this will allow an instance of a Cat to be created with a name
        self.name = name
    def speak(self):
        # defining a function within a class ties this method to an instance of the class
        return 'meow'

my_cat = Cat('Misty')
print(type(my_cat))
print(my_cat.name, my_cat.speak())
print(dir(my_cat))
    
