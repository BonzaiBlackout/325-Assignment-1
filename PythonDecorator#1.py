# this simple python decorator program will be about pizza and toppings
#simply by Arianna Cooper

def add_toppings(func):
    def wrapper():
        print("lets add toppings to your pizza!")
        func()

    return wrapper


@add_toppings
def get_pizza():
    print("Hope you enjoy your pizza!")

get_pizza()
