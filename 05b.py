result = 0

def add(*args):
    """
    This function adds all the numbers passed in as arguments.
    
    Args:
    *args: Variable length argument list of numbers to add.
    """
    global result  # Declare 'result' as global so we can modify it
    for num in args:
        result += num

def print_result():
    """
    This function prints the global variable 'result'.
    """
    global result  # Declare 'result' as global so we can access it
    print(f"The result is {result}")

add(31, 11, 00, 44, 28)  
print_result()  