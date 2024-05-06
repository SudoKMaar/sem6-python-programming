class Number:
    def __init__(self, value):
        self.value = value

    # Overload the "<" operator
    def __lt__(self, other):
        return self.value < other.value

    # Overload the "<=" operator
    def __le__(self, other):
        return self.value <= other.value

    # Overload the "==" operator
    def __eq__(self, other):
        return self.value == other.value

    # Overload the "!=" operator
    def __ne__(self, other):
        return self.value != other.value

    # Overload the ">" operator
    def __gt__(self, other):
        return self.value > other.value

    # Overload the ">=" operator
    def __ge__(self, other):
        return self.value >= other.value

num1 = Number(44)
num2 = Number(31)
print(num1 < num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 >= num2)
