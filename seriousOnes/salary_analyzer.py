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
monthly_saving_goal = int(input("Monthly saving goal: "))
monthly_expense_limit = int(input("Monthly expense limit: "))


'''HEADINGS'''
heading_info = "\n------- EMPLOYEE INFORMATION --------\n"
heading_income = "\n-------- INCOME INFORMATION --------\n"
heading_expense = "\n-------- EXPENSE INFORMATION -------\n"
heading_summary = "\n------------ SUMMARY ------------\n"
heading_financial_situation = "\n-------- FINANCIAL SITUATION -------\n"

'''FORMULA'''
total_income = base_salary + bonus_salary
total_expense = rent + food + transport + other
saved_money = total_income - total_expense
#Income information
income_per_week = total_income / 4 
income_per_day = total_income / 30
income_per_hour = total_income / monthly_working_hours
#Expense information
expense_per_week = total_expense / 4
expense_per_day = total_expense / 30
expense_per_hour = total_expense / monthly_working_hours
#% of stuff out of income
#ptg = percentage
#exp = expense
total_exp_ptg = total_expense * 100 / total_income
food_exp_ptg = food * 100 / total_income
transport_exp_ptg = transport * 100 / total_income
rent_exp_ptg = rent * 100 / total_income
other_exp_ptg = other * 100 / total_income
saved_exp_ptg = saved_money * 100 / total_income
lent_exp_ptg = lent * 100 / total_income
debt_exp_ptg = debt * 100 / total_income
#inc = income
base_inc_ptg = base_salary * 100 / total_income
bonus_inc_ptg = bonus_salary * 100 / total_income
saving_goal_ptg = total_income * 100 / monthly_saving_goal
expense_limit_ptg = total_expense * 100 / monthly_expense_limit


'''PRINT'''
'''Heading'''
print("EMPLOYEE INFORMATION".center(50))

'''Employee Info'''
print(f"\nEmployee Name: {employee_name.title()}\n")
print(f"Employee ID: {employee_id.upper()}\n")
print(f"Current Position: {position.title()}\n")
print(f"Working Schedule: {working_schedule}\n")
print(f"Working Hours: {monthly_working_hours}\n")

'''Heading'''
print("INCOME INFORMATION".center(50))

'''Income Info'''
print(f"Month Name: {month_name.upper()}\n")
print(f"Base Salary: {base_salary} usd\n")
print(f"Bonus Salary: {bonus_salary} usd\n")

'''Heading'''.center(50)
print("EXPENSE INFORMATION".center(50))

'''Expense Info'''
print(f"Rent: {rent} usd\n")
print(f"Food: {food} usd\n")
print(f"Transport: {transport} usd\n")
print(f"Others: {other} usd\n")
print(f"Lent: {lent} usd\n")
print(f"Debt: {debt} usd\n")

'''Heading'''
print("SUMMARY".center(50))

'''Income Summary'''
print(f"Total Income: {total_income} usd\n")
print(f"Income Per:\nWeek   \tDay   \tHour")
print(f"Income per Week: {income_per_week:.1f} usd\n")
print(f"Income per Day {income_per_day:.1f} usd\n")
print(f"Income per Hour {income_per_hour:.1f} usd\n\n")
print(f"Base Salary is {base_inc_ptg:.1f} % of my Income\n")
print(f"Bonus is {bonus_inc_ptg:.1f} % of my Income\n")

'''Expense Summary'''
print(f"Total Expense: {total_expense:.1f} usd\n")
print(f"Expense is {total_exp_ptg:.1f} % of my Income\n")
print(f"Rent is {rent_exp_ptg:.1f} % of my Income\n")
print(f"Food is {food_exp_ptg:.1f} % of my Income\n")
print(f"Transport is {transport_exp_ptg:.1f} % of my Income\n")
print(f"Other expenses are {other_exp_ptg:.1f} % of my Income\n")
print(f"Expense Per:\nWeek   \tDay   \tHour")
print(f"Expense per Week: {expense_per_week:.1f} usd\n")
print(f"Expense per Day {expense_per_day:.1f} usd\n")
print(f"Expense per Hour {expense_per_hour:.1f} usd\n")

'''HEADING'''
print("FINANCIAL SITUATION".center(50))

'''Financial Situation'''
print(f"Saving Goal: {monthly_saving_goal} usd")
print(f"Saved Money: {saved_money} usd\n")

print(f"Percentage of Saving Goal: {monthly_saving_goal:.1f} %")
print(f"Percentage of Saved Money: {saved_exp_ptg:.1f} %\n\n")

print(f"Expense Limit: {monthly_expense_limit} usd")
print(f"Total Expense: {total_expense:.1f} usd\n")

print(f"Percentage of Expense Limit: {expense_limit_ptg:.1f} %")
print(f"Percentage of Total Expense: {total_exp_ptg:.1f} %\n")

print(f"I lent {lent_exp_ptg:.1f} % of my Income\n")
print(f"{debt_exp_ptg:.1f} % of my Income is a Debt\n")
