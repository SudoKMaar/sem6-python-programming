import math

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for _ in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {i+1} : ")) for i in range(self.n)]

    def displaySides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def displayArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(f"The area of the triangle is {area}")

t = Triangle()
t.inputSides()
t.displaySides()
t.displayArea()
