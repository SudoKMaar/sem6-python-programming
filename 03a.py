lst = list(map(int, input("Enter a list of integers separated by space: ").split()))

# (1) Display the number of elements in the list
print(f"Number of elements: {len(lst)}")

# (2) Display minimum and maximum element in the list
print(f"Minimum element: {min(lst)}")
print(f"Maximum element: {max(lst)}")

# (3) Display sum of square of all the elements in the list
print(f"Sum of squares: {sum(i**2 for i in lst)}")

# (4) Add a new element at end and display the list
lst.append(10)
print(f"List after adding an element at the end: {lst}")

# (5) Add a new element at given index and display list
index = 2
lst.insert(index, 20)
print(f"List after adding an element at index {index}: {lst}")

# (6) Display the occurrence of given element in the list
element = 31
print(f"Occurrence of {element}: {lst.count(element)}")

# (7) Remove the given element in the list
lst.remove(element)
print(f"List after removing {element}: {lst}")

# (8) Add elements from a new list to the given list
new_lst = [31, 44, 11]
lst += new_lst
print(f"List after adding elements from a new list: {lst}")

# (9) Sort the given list & reverse the given list
lst.sort()
print(f"Sorted list: {lst}")
lst.reverse()
print(f"Reversed list: {lst}")

# (10) Perform slicing, concatenation and multiplication operation
print(f"Sliced list (first 3 elements): {lst[:3]}")
print(f"Concatenated list: {lst + [93, 10, 97]}")
print(f"Multiplied list (first 3 elements repeated 3 times): {lst[:3]*3}")