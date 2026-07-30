#salary analyzer 

name = input("Employee name:")
base_salary = int(input("Base salary: "))
bonus_salary = int(input("Bonus salary: "))
rent = int(input("Rental cost: "))
food = int(input("Food cost: "))
transport = int(input("Transportation cost: "))

heading_salary = f"\n----------- SALARY ANALYZER -------------\n"
heading_income = f"\n----------- INCOME -------------\n"
heading_expense = f"\n----------- EXPENSE -------------\n"
heading_summary = f"\n----------- SUMMARY -------------\n"

total_income = base_salary + bonus_salary
total_expense = food + rent + transport

money_saved = total_income - total_expense

print(heading_salary)
print(f"\nName: {name}\n")

print(heading_income)
print(f"Base Salary: {base_salary} uzs\nBonus: {bonus_salary} uzs\nTotal Income: {total_income} uzs\n")

print(heading_expense)
print(f"Rent: {rent} uzs\nFood: {food} uzs\nTransportation: {transport} uzs\nTotal Expense: {total_expense} uzs\n")

print()

print(f"Money saved: {money_saved} uzs\n")

print("===========================================================")