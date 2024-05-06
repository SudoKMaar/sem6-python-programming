class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no, university, branch):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.university = university
        self.branch = branch

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}, University: {self.university}, Branch: {self.branch}")

    def change_branch(self, new_branch):
        self.branch = new_branch
        print(f"Branch changed to {new_branch}")

# Create a Student object
s = Student("Abhishek Kumar", 19, "21BCA31", "Lingayas Vidyapeeth", "Computer Science")

# Display student information
s.display()

# Change branch
s.change_branch("Computer Applications")
