def find_student(roll_no):
    try:
        with open('student.txt', 'r') as f:
            for line in f:
                if line.split()[0] == roll_no:
                    return ' '.join(line.split()[1:])
    except FileNotFoundError:
        print("The file student.txt does not exist.")
        return None

    return "roll no not present in the file"

roll_no = input("Enter the roll number: ")
print(find_student(roll_no))
