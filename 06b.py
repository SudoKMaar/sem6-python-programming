class Employee:
    no_of_employees = 0
    annual_incr = 0.05 

    def __init__(self, name, salary):
        Employee.no_of_employees += 1
        self.name = name
        self.empid = Employee.no_of_employees
        self.salary = salary

    def display(self):
        print(f"Employee ID: {self.empid}, Name: {self.name}, Salary: {self.salary}")

    def increase_salary(self):
        self.salary += self.salary * Employee.annual_incr
        print(f"New Salary after increment: {self.salary}")

    @classmethod
    def change_annual_incr(cls, new_incr):
        cls.annual_incr = new_incr

emp1 = Employee("Abhishek", 50000)
emp1.display()
emp1.increase_salary()

emp2 = Employee("KMaar", 60000)
emp2.display()
emp2.increase_salary()

Employee.change_annual_incr(0.10)  # Change the annual increment to 10%

emp1.increase_salary()
emp2.increase_salary()
