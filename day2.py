import example_package
#My module

example_package.randomfunction()

import sys

print('\n'.join(sys.path))

# randomfunction2

# Global vs Local variables
def print_obj():
    print(eggs)
    # What if I want to change it?
    # eggs = "Chicken"
    print(eggs)

global eggs
eggs = "Eggs!"
print_obj()
eggs = "Spam"
print(eggs)

# First class objects


def func(x):
    def func(y):
        return x + y
    return func
    # return lambda y: x+y

a = func(1)
print(a(2))
print(a(3))

# Tuples

tuple_a = ()

tuble_b = (1,)

tuple_c = (1)

len(tuple_a)

some_list = [1, 2, 3]

tuple(some_list)

a, b = [1, 2]

a, *b = 1, 2, 3, 4, 5

b, a = a, b

# Dicts

some_dict = {"Anna": 23, "Dana": 21}

another_dict = {(1, 2, 3): "Numbers!"}

#Map
print(list(map(lambda x:x**x,[1,2,3])))

x = map(lambda x:x**x,[1,2,3])

    #next

for i in x:
    print(i)

#Filter

for i in filter(lambda x:x % 2,[1,2,3,4,5,6,7,8,9,10]):
    print(i)

#Reduce

from functools import reduce

print(reduce( lambda x, y: x + y, [1, 2, 3, 4] ))

# args kwargs


def func(a, b, c):
    print(a, b, c)

args = [1, 2, 3]
func(*args)


def func(*args):
    print(args)

func(1, 2, 3)

def func(some_arg,*args, **kwargs):
    print(some_arg)
    print("Args: ", args)
    print("KWArgs: ", kwargs)

func(1,2,3,anna=1,dana=2)


# Classes

class Mammal:
    #class attribute​
    type_of_mamma = 'Human'

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        print("Mammal")

    def __str__(self):
        return "This works with print"

    def sing(self):
        return("Lala")

anna = Mammal("Anna", 24)
print(anna.name)
# print(anna.__age)
# print(anna._Mammal__age)

print(anna)

# Multiple Inheritance

class Animal:

    def __init__(self, name):
        self.name = name
        print("Argh")


class Cow(Animal, Mammal):

    def __init__(self, name):
        super().__init__(name)
        self.x = name
        # Animal.__init__(self)
        # Animal.name = x

    def __lt__(self, other):
        if len(self.x) < len(other.x):
            return True
        else:
            False

# class Heifer(Cow):
#
#     def __init__(self, name):
#         Cow.x = name


cow = Cow("Molly")
print(cow.x)

cow2 = Cow("Milicent")

print(cow < cow2)
