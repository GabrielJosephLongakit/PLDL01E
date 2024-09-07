#initialization
final_grade = 0
student_name = ""
final_quiz = 0
final_assignment = 0
final_project = 0
final_exam = 0
equivalent_grade = 0

#input
student_name = str(input("Please enter your Student Name: "))
final_quiz = float(input("Please input your final quiz grade: "))
final_assignment = float(input("Please input your final assignment grade: "))
final_project = float(input("Please input your final project grade:"))
final_exam = float(input("Please enter your final exam grade: "))


#calculate
final_grade = (final_quiz *.30)+(final_assignment * .10)+(final_exam * .40)+(final_project * .20)

#if then
if 98 <= final_grade <= 100:
    equivalent_grade = 4.00
elif 95 <= final_grade <= 97:
    equivalent_grade = 3.75
elif 92 <= final_grade <= 94:
    equivalent_grade = 3.50
elif 89 <= final_grade <= 91:
    equivalent_grade = 3.25
elif 86 <= final_grade <= 88:
    equivalent_grade = 3.00
elif 83 <= final_grade <= 85:
    equivalent_grade = 2.75
elif 80 <= final_grade <= 82:
    equivalent_grade = 2.50
elif 77 <= final_grade <= 79:
    equivalent_grade = 2.25
elif 74 <= final_grade <= 76:
    equivalent_grade = 2.00
elif 71 <= final_grade <= 73:
    equivalent_grade = 1.75
elif 68 <= final_grade <= 70:
    equivalent_grade = 1.50
elif 64 <= final_grade <= 67:
    equivalent_grade = 1.25
elif 60 <= final_grade <= 63:
    equivalent_grade = 1.00
elif 60 > final_grade:
    equivalent_grade = 0.00

#print the grades
print("Students Name:", student_name)
print("Final Quiz Grade:", final_quiz)
print("Final Assignment Grade:", final_assignment)
print("Final Project Grade:", final_project)
print("Final Exam Grade:", final_exam)
print("Final Grade:", final_grade)
print("Grading Remarks:", equivalent_grade)
