# Assignements in Python
x = 3
y = x
# x and y refer to the same object
print(id(x),id(y))
y = 2
print(id(x),id(y))
#========================================
# Global vs Local variables
def print_obj():
    print(eggs)
    # What if I want to change it?

global eggs
eggs = "Eggs!"
print_obj()
eggs = "Spam"
print(eggs)

#========================================

def func(a,b,c):
    print(a,b,c)

args = [1,2,3]
func(*args)

def func(*args):
    print(args)

func(1,2,3)
