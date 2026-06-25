weight = float(input("What is your weight in kg: "))
height = float(input("What is your height in meters: "))

bmi = weight / (height * height)

print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
