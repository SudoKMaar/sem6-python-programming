def greet(name, greeting="Hello"):
    """
    This function greets the person passed in as a parameter with the greeting word.
    If no greeting word is provided, it will use "Hello" as a default greeting.
    
    Args:
    name (str): The name of the person to greet.
    greeting (str, optional): The greeting word. Defaults to "Hello".
    """
    print(f"{greeting}, {name}!")

greet("Abhishek")  # Uses the default greeting
greet("KMaar", greeting="Good morning")  # Uses a custom greeting
