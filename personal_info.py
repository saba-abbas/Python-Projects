user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_city = input("Enter your city: ")
course = input("Enter your course: ")
monthly_income = float(input("Enter your monthly income: "))

if user_age < 18:
    print("You are a student")
elif user_age <= 25:
    print("You are a young adult")
else:
    print("You are an adult")

if monthly_income > 50000:
    print("You are earning well")
elif monthly_income >= 20000:
    print("You are earning average")
else:
    print("You are just starting out")

print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"City: {user_city}")
print(f"Course: {course}")
print(f"Monthly Income: {monthly_income}")
