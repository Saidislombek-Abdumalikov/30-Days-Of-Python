#salary analyzer 

name = input("Employee name:")
employee_id = input("Employee ID:")
position = input("Position: ")
shift = input("Shift (day/night): ")
working_hours = int(input("Working hours per month: "))
salary_month = input("Salary month: (eg.,June): ")
base_salary = int(input("Base salary: "))
bonus_salary = int(input("Bonus salary: "))
rental = int(input("Rental cost: "))
food = int(input("Food cost: "))
transport = int(input("Transportation cost: "))
rent = int(input("Rented money: "))
lending = int(input("Money lent to others: "))
debt = int(input("Debt: "))

heading_info= f"\n----------- EMPLOYEE INFO -------------\n"
heading_income = f"\n----------- INCOME -------------\n"
heading_expense = f"\n----------- EXPENSE -------------\n"
heading_summary = f"\n----------- FINANCIAL SITUATION -------------\n"

total_income = base_salary + bonus_salary
total_expense = food + rent + transport +rental

money_saved = total_income - total_expense

income_per_hour = total_income / working_hours




print(heading_info)
print(f"\nName: {name}\n")
print(f"ID: {employee_id}\n")
print(f"Position: {position}\n")
print(f"Shift: {shift}\n")
print(f"Salary month: {salary_month}\n")

print(heading_income)
print(f"Monthly Salary: {base_salary} uzs\nBonus: {bonus_salary} uzs\nTotal Income: {total_income} uzs\nIncome per hour: {income_per_hour:.1f}")

print(heading_expense)
print(f"Rented money: {rent} uzs\nRental cost: {rental} uzs\nFood: {food} uzs\nTransportation: {transport} uzs\nTotal Expense: {total_expense} uzs\n")

print(heading_summary)

print(f"Money saved: {money_saved} uzs\nDebt: {debt}\nMoney lent to others: {lending}")

print("===========================================================")