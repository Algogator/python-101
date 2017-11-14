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
