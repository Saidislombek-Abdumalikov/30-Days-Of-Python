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
'''HEADING'''
heading_total_bill = "\n-------------------------\nTOTAL BILL\n------------------------"
heading_restaurant_bill = "\n====================\nRESTAURANT BILL\n===================="
'''FORMULA'''
total_bill = meal_price + drink_price
'''PRINT'''
print("\n",heading_restaurant_bill)
print(f"Restaurant: {restaurant_name}")
print(f"Customer: {customer_name}")
print(f"Waiter: {waiter_name}")
print(f"Table: {table_number}\n")
print(f"Meal: {meal_name}")
print(f"Drink: {drink_name}\n")
print(f"Meal Price: {meal_price} USD")
print(f"Drink Price: {drink_price} USD\n")
print("\n",heading_total_bill)
print(f"Total Bill: {total_bill} USD")