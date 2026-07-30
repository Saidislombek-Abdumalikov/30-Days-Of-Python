#electricity bill estimator

customer_name = input("Customer name: ")
pre_meter = int(input("Previous meter: "))
curr_meter = int(input("Current meter: "))
price = int(input("Price per kWh: "))
budget = int(input("Monthly budget: "))

e_used = curr_meter - pre_meter
total_bill = e_used * price
remaining_budget = budget - total_bill
avg_e_used_day = e_used / 30
avg_m_used_day = total_bill / 30
percentage_budget_spent = total_bill * 100 / budget
percentage_budget_remaining = remaining_budget * 100 / budget

print()
print("---------- ELECTRICITY BILL REPORT ----------")
print()

print(f"Customer: {customer_name}")
print()

print(f"Previous Reading: {pre_meter} kWh")
print()

print(f"Current Reading: {curr_meter} kWh")
print()

print(f"Electricity used: {e_used} kWh")
print()

print(f"Average electricity used per day: {avg_e_used_day} kWh")
print()

print(f"Price per kWh: {price}")
print()

print(f"Average money spent per day: {avg_m_used_day} uzs")
print()

print(f"Total Bill: {total_bill} uzs")
print()

print(f"Remaining budget: {remaining_budget} uzs")
print()

print(f"Percentage of the budget spent : {percentage_budget_spent} %")
print()

print(f"Percentage of the budget remaining : {percentage_budget_remaining} %")
print()


print("=============================================")