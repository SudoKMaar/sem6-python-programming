class Length:
    def __init__(self, feet=0, inches=0):
        self.feet = feet
        self.inches = inches

    # Overload the "+" operator
    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches
        # Convert inches to feet if total_inches is greater than or equal to 12
        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches = total_inches % 12
        return Length(total_feet, total_inches)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

length1 = Length(11, 44)
length2 = Length(28, 31)

total_length = length1 + length2
print(total_length)
