#travel planner
#difficulty  *

destination = input("Destination city: ")
num_night = int(input('Number of nights: '))
hotel_price = int(input("Hotel price per night: "))
food_budget = int(input("Food budget per day: "))
transport_cost = int(input("Transportation cost: "))
other_ex = int(input("Other expenses: "))
budget = int(input("Budget: "))

hotel_cost = hotel_price * num_night
food_cost = food_budget * num_night

total = num_night * (hotel_price + food_budget) + transport_cost + other_ex
remaining_money = budget - total
avg_per_day = total / num_night

print()

print("--------- TRAVEL PLAN ---------")
print()

print(f"Destination: {destination}")
print()

print(f"Days: {num_night} ")
print()

print(f"Hotel cost: {hotel_cost} uzs")
print()

print(f"Food cost: {food_cost} uzs")
print()

print(f"Transportation: {transport_cost} uzs")
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