class MyClass:
    """
    This is a sample class to demonstrate the use of built-in class attributes and special methods.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"MyClass object with name: {self.name}"

    def __del__(self):
        print(f"MyClass object with name {self.name} is being deleted.")

# Create an object of MyClass
obj = MyClass("Test")

# Use built-in class attributes
print("Documentation string (__doc__):", MyClass.__doc__)
print("Dictionary containing the class's namespace (__dict__):", MyClass.__dict__)
print("Class name (__name__):", MyClass.__name__)
print("Module name in which the class is defined (__module__):", MyClass.__module__)
print("A possibly empty tuple containing the base classes (__bases__):", MyClass.__bases__)

# Use special methods
print("String representation of the object (__str__):", str(obj))

# Use built-in function isinstance()
print("Check if obj is an instance of MyClass:", isinstance(obj, MyClass))

# Delete the object
del obj
