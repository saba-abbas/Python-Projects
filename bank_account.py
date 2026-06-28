name = input("your full name")
account_number = int(input("your account number"))
current_balance = float(input("your current balance"))
withdraw = float(input("how much u want to withdraw"))

if withdraw > current_balance:
    print(f"insufficient balance your current balance is {current_balance}")
elif withdraw == current_balance: 
    total = current_balance - withdraw
    print(f"you are withdrawing everything your remaining balance is {total}")
elif withdraw < current_balance:
    total = current_balance - withdraw
    print(f"Withdrawal successful! Remaining balance: is {total}")

print(f" Name:{name}")  
print(f"Account Number{account_number}")
print(f"Current balance {current_balance}")
print(f"withdraw:{withdraw}")    
