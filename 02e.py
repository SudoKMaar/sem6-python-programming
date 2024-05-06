binary_num = input("Enter a binary number: ")
decimal_num = 0

for digit in binary_num:
    decimal_num = decimal_num*2 + int(digit)

print(f"The decimal number is {decimal_num}.")
