
#Day 1 - 30DaysOfPython Challenge AGE in Days/Hours/Minutes/Seconds

age = input("Enter AGE: ")


age = int(age)

y_to_d = age * 365
y_to_h = y_to_d * 24
y_to_m = y_to_d * 60
y_to_s = y_to_m * 60


print("It's been: ", y_to_d, "days")
print("It's been: ", y_to_h, "hours")
print("It's been: ", y_to_m, "minutes")
print("It's been: ", y_to_s, "seconds")
