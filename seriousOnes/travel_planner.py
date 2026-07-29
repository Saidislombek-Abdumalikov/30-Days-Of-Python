#travel planner
#difficulty  *

destination = input("Destination city: ")
num_night = int(input('Number of nights: '))
hotel_price = int(input("Hotel price per night: "))
food_budget = int(input("Food budget per day: "))
transport_cost = int(input("Transportation cost: "))
other_ex = int(input("Other expenses: "))
budget = int(input("Budget: "))

hotel_cost = hotel_price * num_night                        #total money spent on booking hotel
food_cost = food_budget * num_night                         #total money spent on food

total = num_night * (hotel_price + food_budget) + transport_cost + other_ex       #total money spent on the trip
remaining_money = budget - total                            #remaining money from budget
avg_per_day = total / num_night                             #average money spent for travelling per day
hotel_percentage = float(hotel_cost * 100 / total)          #percentage of money spent on booking hotel
food_percentage = float(food_cost * 100 / total)            #percentage of money spent on food
transport_percentage = float(transport_cost * 100 / total)  #percentage of monet spent on transportation


print()

print("--------- TRAVEL PLAN ---------")
print()

print(f"Destination: {destination}")
print()

print(f"Days: {num_night} ")
print()

print(f"Hotel cost: {hotel_cost} uzs")
print(f"Hotel takes {hotel_percentage} of your total trip cost.")
print()

print(f"Food cost: {food_cost} uzs")
print(f"Food takes {food_percentage} of your total trip cost.")
print()

print(f"Transportation: {transport_cost} uzs")
print(f"Transportation takes {transport_percentage} of your total trip cost.")
print()

print(f"Other expenses: {other_ex} uzs")
print()

print("----------------------------------------")
print()

print("Total Trip Costs: ")
print(total)
print()

print("Average Per Day: ")
print(avg_per_day)
print()

print("Remaing Money: ")
print(remaining_money)   # no if statement, even it shows negative 
print()

print("===========================================")