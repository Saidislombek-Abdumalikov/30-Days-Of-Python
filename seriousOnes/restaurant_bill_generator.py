  #Restaurant Bill Generator

'''INPUT'''
customer_name = input("Customer Name: ").strip().title()
table_number = int(input("Table Number: "))
waiter_name = input("Waiter Name: ").strip().title()
restaurant_name = input("Restaurant Name: ").strip().title()
meal_name = input("Meal Name: ").strip().title()
drink_name = input("Drink Name: ").strip().title()
meal_price = int(input("Meal Price(USD): "))
drink_price = int(input("Drink Price(USD): "))
meal_quantity = int(input("Meal Quantity: "))
drink_quantity = int(input("Drink Quantity: "))



'''HEADING'''
heading_total_bill = "\n-------------------------\nTOTAL BILL\n------------------------"
heading_restaurant_bill = "\n====================\nRESTAURANT BILL\n===================="



'''FORMULA'''
total_bill = meal_price + drink_price
total_meal = meal_quantity * meal_price
total_drink = drink_quantity * drink_price



'''PRINT'''
print("\n",heading_restaurant_bill)
print(f"Restaurant: {restaurant_name}")
print(f"Customer: {customer_name}")
print(f"Waiter: {waiter_name}")
print(f"Table: {table_number}\n")

print(f"Meal: {meal_name}")
print(f"Meal Price: {meal_price} USD")
print(f"Meal Quantity: {meal_quantity}")

print(f"Drink: {drink_name}")
print(f"Drink Price: {drink_price} USD")
print(f"Drink Quantity: {drink_quantity}\n")

print("\n",heading_total_bill)
print(f"Total Meal: {total_meal} USD")
print(f"Total Drink: {total_drink} USD\n")
print(f"Total Bill: {total_bill} USD")