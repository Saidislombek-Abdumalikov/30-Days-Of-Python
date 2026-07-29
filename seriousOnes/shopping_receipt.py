#shopping receipt

customer_name = input("Customer name: ")
print()

pr1_name = input("Product 1 name: ")
pr1_price = int(input(f"Price of the {pr1_name}: "))
pr1_quantity = int(input(f"Quantity of the {pr1_name}: "))
print()

pr2_name = input("Product 2 name: ")
pr2_price = int(input(f"Price of the {pr2_name} : "))
pr2_quantity = int(input(f"Quantity of the {pr2_name} : "))
print()

pr3_name = input("Product 3 name: ")
pr3_price = int(input(f"Price of the {pr3_name}: "))
pr3_quantity = int(input(f"Quantity of the {pr3_name}: "))


cost1 = pr1_quantity * pr1_price
cost2 = pr2_quantity * pr2_price
cost3 = pr3_quantity * pr3_price

total_cost = cost1 + cost2 + cost3
total_items = pr1_quantity + pr2_quantity + pr3_quantity


print()
print()
print("---------- SHOPPING RECEIPT ----------")
print()

print(f"Customer name: {customer_name}")
print()

print(f"1 - {pr1_name} x {pr1_quantity}")
print(f"2 - {pr2_name} x {pr2_quantity}")
print(f"3 - {pr3_name} x {pr3_quantity}")
print()

print("----- Cost of each product -----")
print()
print(f"1 -  {pr1_quantity} * {pr1_price} = {cost1}")
print(f"2 -  {pr2_quantity} * {pr2_price} = {cost2}")
print(f"3 -  {pr3_quantity} * {pr3_price} = {cost3}")
print()

print("--------- TOTAL BILL ---------")
print()

print(f"Total number of items: {total_items}")
print()

print(f"Total bill is: {total_cost} uzs")
print()
