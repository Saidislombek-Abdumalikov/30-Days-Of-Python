#Restaurant Bill Generator

'''INPUT'''
customer_name = input("Customer Name: ").strip().title()
table_number = int(input("Table Number: "))
waiter_name = input("Waiter Name: ").strip().title()
restaurant_name = input("Restaurant Name: ").strip().title()
meal_name = input("Meal Name: ").strip().title()
drink_name = input("Drink Name: ").strip().title()
meal_price = int(input("Meal Price: "))
drink_price = int(input("Drink Price: "))


'''HEADING'''
heading_total_bill = "\nTOTAL BILL\n"


'''FORMULA'''
total_bill = meal_price + drink_price

'''PRINT'''
print("\n",heading_total_bill)

print(f"Total Bill: {total_bill}")