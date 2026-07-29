#fuel cost calculator


#input
car_name = input("Car Model: ")
trip_distance = int(input("Trip distance (km): "))
avg_speed = int(input("Average driving speed (km/h): "))
fuel_consumption = int(input("Fuel consumption (litres per 100 km): "))
fuel_price = float(input("Fuel price (per liter): "))
budget= float(input("Budget (uzs): "))
#input

fuel_needed = trip_distance * fuel_consumption / 100          #calculates the liter of fuel needed for trip
total_trip_cost = fuel_needed * fuel_price                    #calcualtes the total cost  
time_to_reach_h = trip_distance / avg_speed                   #calculates the time in hours
time_to_reach_M = int(time_to_reach_h * 60)                   #calcualtes the time in minutes
remaining_money = budget - total_trip_cost                    #calculates the money left

print()
print("--------- FUEL TRIP REPORT --------")
print() 

print(f"Car Model: {car_name}")
print()

print(f"Average speed of the car: {avg_speed} km/h")
print()

print(f"Total distance in km: {trip_distance}")
print()

print(f"Expected time to reach A to B: {time_to_reach_h} hours or {time_to_reach_M} minutes")
print()

print(f"Fuel needed: {fuel_needed}")
print()

print(f"Total trip cost: {total_trip_cost} uzs")
print()

print(f"Remaining money: {remaining_money} uzs")
print()

print("============================")