'''INPUT'''
employee_name = input("Employee name:")
employee_id = input("Employee ID: ")
position = input("Employee postion: ")
#work
working_schedule = input("Working schedule (day/night): ")
monthly_working_hours = int(input("Working hours: "))
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
total_income = base_salary + bonus_salary
total_expense = rent + food + transport + other
saved_money = total_income - total_expense
#income-per
income_per_week = total_income / 4 
income_per_day = total_income / 30
income_per_hour = total_income / monthly_working_hours
#expensee-per
expense_per_week = total_expense / 4
expense_per_day = total_expense / 30
expense_per_hour = total_expense / monthly_working_hours

'''PRINT'''
print(heading_info)

print(f"\nEmployee Name: {employee_name}\n")
print(f"Employee ID: {employee_id}\n")
print(f"Current Position: {position}\n")
print(f"Working Schedule: {working_schedule}\n")
print(f"Working Hours: {monthly_working_hours}\n")

print(heading_income)

print(f"Month Name: {month_name}\n")
print(f"Base Salary: {base_salary} usd\n")
print(f"Bonus Salary: {bonus_salary} usd\n")


print(heading_expense)

print(f"Rent: {rent} usd\n")
print(f"Food: {food} usd\n")
print(f"Transport: {transport} usd\n")
print(f"Others: {other} usd\n")
print(f"Lent: {lent} usd\n")
print(f"Debt: {debt} usd\n")


print(heading_summary)

print(f"Total Income: {total_income} usd\n")
print(f"Income Per:\nWeek   \tDay   \tHour")
print(f"Income per Week: {income_per_week:.1f} usd\n")
print(f"Income per Day {income_per_day:.1f} usd\n")
print(f"Income per Hour {income_per_hour:.1f} usd\n\n")

print(f"Total Expense: {total_expense} usd\n")
print(f"Expense Per:\nWeek   \tDay   \tHour")
print(f"Expense per Week: {expense_per_week:.1f} usd\n")
print(f"Expense per Day {expense_per_day:.1f} usd\n")
print(f"Expense per Hour {expense_per_hour:.1f} usd\n")

print(f"Saved Money: {saved_money}")