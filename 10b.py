try:
    # Open the file in read-only mode
    with open('test.txt', 'r') as f:
        # Read data from the file
        data = f.read()
        print(f"Data from the file: {data}")
        # Try to write data to the file
        f.write("This will cause an error.")
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: The file is read-only, so data cannot be written to it.")
except Exception as e:
    print(f"Error: {str(e)}")
