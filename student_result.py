student_name = input("Enter your name: ")
english = float(input("Enter your English marks: "))
science = float(input("Enter your Science marks: "))
maths = float(input("Enter your Maths marks: "))

total_marks = english + science + maths
percentage = (total_marks / 300) * 100

if percentage >= 90:
    print(f"{student_name} - Grade A - Distinction")
elif percentage >= 70:
    print(f"{student_name} - Grade B - Merit")
elif percentage >= 50:
    print(f"{student_name} - Grade C - Pass")
else:
    print(f"{student_name} - Grade F - Fail")

print(f"Total marks: {total_marks}")
print(f"Percentage: {percentage}%")
