def divide(arg1, arg2):
    try:
        result = arg1 / arg2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both arguments must be numbers.")
    except Exception as e:
        print(f"Error: {str(e)}")
    else:
        print(f"The result is {result}.")
    finally:
        print("End of division operation.")

try:
    arg1 = float(input("Enter the first number: "))
    arg2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Input must be a number.")
else:
    divide(arg1, arg2)
