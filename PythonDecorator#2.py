# this simple python decorator program will half the number read in
#simply by Arianna Cooper

def calculate_half(func):
    def wrapper(*args):
        result= func(*args)
        total = result / 2
        print(total)

    return wrapper


@calculate_half
def get_num(num):
    return num
    
get_num(8)