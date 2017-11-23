def dec(function):

    def wrapper():
        function()
    return wrapper

@dec
def some_function():
    print("Anna")

some_function()
