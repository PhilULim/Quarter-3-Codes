students = []

for i in range(3):
    student_dict = {}
    input_name = input("Enter your name:")
    input_age = (input("Enter your age:"))
    input_grade = input("Enter your grade:")

    student_dict["Name"] = input_name
    student_dict["Age"] = input_age
    student_dict["Grade"] = input_grade
    students.append(student_dict)

len_students = len(students)
for i in range(len_students):
    print ("Class Directory", "\n",students[i])


