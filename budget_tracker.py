#budget_tracker.py
#my first mini project

#User Salary
income = float(input("Enter Salary: "))

expenses = {
     "car": 1200,
     "food": 2000,
     "creditcard": 2000
     
}

#User Expenses
car = float(input("Enter Car amount: "))
food = float(input("Enter Food amount): "))
waterandElec = float(input("Enter Water and Electricity amount): "))
creditCard = float(input("Enter Credit Card payment): "))

#Calculate total Expenses
total_expenses  = car + food + waterandElec + creditCard

#Calculate remaining balance
total_remaining = income - total_expenses

#Results
print("\n--- Salary Budget ---")
print(f"Total Income: AED {income}")
print(f"Total Expenses: AED {total_expenses}")
print(f"Total Remaining: AED {total_remaining}")

if total_remaining < 0:
     print("You are over budget)")
elif total_remaining == 0:
     print("0 Balance left)")
else:
     print("You are within Budget)")

#Loop
for item, amount in expenses.items():
    print(f"{item}: AED {amount}")

