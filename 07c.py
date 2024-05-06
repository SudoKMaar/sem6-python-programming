class Parent1:
    def __init__(self):
        self.name1 = "Parent1"

    def display1(self):
        print(f"I am {self.name1}")

class Parent2:
    def __init__(self):
        self.name2 = "Parent2"

    def display2(self):
        print(f"I am {self.name2}")

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        self.name = "Child"

    def display(self):
        print(f"I am {self.name}")
        self.display1()
        self.display2()

c = Child()
c.display()
