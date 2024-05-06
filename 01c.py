marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

if average >= 90:
    print("Grade: O")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 50:
    print("Grade: D")
elif average >= 40:
    print("Grade: P")
else:
    print("Grade: F")
