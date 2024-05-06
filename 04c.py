java_course = {"Anmol", "Rahul", "Priyanka", "Pratik"}
python_course = {"Rahul", "Ram", "Nazim", "Vishal"}

# 1) Number of students enrolled for Python course
print(f"Number of students enrolled for Python course: {len(python_course)}")

# 2) Number of students enrolled for Java course only
java_only = java_course - python_course
print(f"Number of students enrolled for Java course only: {len(java_only)}")

# 3) Number of students enrolled for Python course only
python_only = python_course - java_course
print(f"Number of students enrolled for Python course only: {len(python_only)}")

# 4) Number of students enrolled for both Java and Python courses
both_courses = java_course & python_course
print(f"Number of students enrolled for both Java and Python courses: {len(both_courses)}")

# 5) Number of students enrolled for either Java or Python courses but not both
either_course = java_course ^ python_course
print(f"Number of students enrolled for either Java or Python courses but not both: {len(either_course)}")

# 6) Number of students enrolled for either Java or Python
any_course = java_course | python_course
print(f"Number of students enrolled for either Java or Python: {len(any_course)}")
