#electricity bill estimator

customer_name = input("Customer name: ")
pre_meter = int(input("Prvious meter: "))
curr_meter = int(input("Current meter: "))
price = int(input("Price per kWh: "))
budget = int(input("Monthly budget: "))

e_used = curr_meter - pre_meter
total_bill = e_used * price
remaining_budget = budget - total_bill

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

print(f"Price per kWh: {price}")
print()

print(f"Total Bill: {total_bill} uzs")
print()

print(f"Remaining budget: {remaining_budget} uzs")
print()

print("=============================================")