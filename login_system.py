username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "Saba" and password == "python123":
    print("Login successful! Welcome Saba!")
elif username == "Saba" and password != "python123":
    print("Wrong password! Try again!")
else:
    print("Username not found!")
