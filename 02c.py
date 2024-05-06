num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while(num2):
    num1, num2 = num2, num1 % num2

print(f"The GCD of {num1} and {num2} is {num1}.")
