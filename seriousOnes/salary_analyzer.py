#salary analyzer 

'''name = input("Employee name:")
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

print("===========================================================")'''

'''INPUT'''
employee_name = input("Employee name:")
employee_id = input("Employee ID: ")
position = input("Employee postion: ")
#work
working_schedule = input("Working schedule (day/night): ")
working_hours = int(input("Working hours: "))
#month
month_name = input("Month name (eg.,June): ")
#salary
base_salary = int(input("Monthly salary (usd): "))
bonus_salary = int(input("Bonus salary (usd): "))
#expense
rent = int(input("Rent for a flat (usd): "))
food = int(input("Food (usd): "))
transport =  int(input("Transportation (usd): "))
other = int(input("Others (usd): "))
#financial situation
lent = int(input("Lent (usd): "))
debt = int(input("Debt (usd): "))

'''HEADINGS'''
heading_info = "\n------- EMPLOYEE INFORMATION --------\n"
heading_income = "\n-------- INCOME INFORMATION --------\n"
heading_expense = "\n-------- EXPENSE INFORMATION -------\n"
heading_summary = "\n------------ SUMMARY ------------\n"

'''FORMULA'''
total_income = base_salary + bonus_salary + debt
total_expense = rent + food + transport + other + lent
saved_money = total_income - total_expense
#income-per
income_per_week = total_income / 4 
income_per_day = total_income / 30
income_per_hour = total_income / working_hours
#expensee-per
expense_per_week = total_expense / 4
expense_per_day = total_expense / 30
expense_per_hour = total_expense / working_hours

'''PRINT'''
print(heading_info)

print(f"\nEmployee Name: {employee_name}\n")
print(f"Employee ID: {employee_id}\n")
print(f"Current Position: {position}\n")
print(f"Working Schedule: {working_schedule}\n")
print(f"Working Hours: {working_hours}\n")

print(heading_income)

print(f"Month Name: {month_name}\n")
print(f"Base Salary: {base_salary} uzs\n")
print(f"Bonus Salary: {bonus_salary} uzs\n")


print(heading_expense)

print(f"Rent: {rent} uzs\n")
print(f"Food: {food} uzs\n")
print(f"Transport: {transport} uzs\n")
print(f"Others: {other} uzs\n")
print(f"Lent: {lent} uzs\n")
print(f"Debt: {debt} uzs\n")


print(heading_summary)

print(f"Total Income: {total_income} uzs\n")
print(f"Income Per:\nWeek   \tDay   \tHour")
print(f"Income per Week: {income_per_week:.1f} uzs\n")
print(f"Income per Day {income_per_day:.1f} uzs\n")
print(f"Income per Hour {income_per_hour:.1f} uzs\n\n")

print(f"Total Expense: {total_expense} uzs\n")
print(f"Expense Per:\nWeek   \tDay   \tHour")
print(f"Expense per Week: {expense_per_week:.1f} uzs\n")
print(f"Expense per Day {expense_per_day:.1f} uzs\n")
print(f"Expense per Hour {expense_per_hour:.1f} uzs\n")

print(f"Saved Money: {saved_money}")