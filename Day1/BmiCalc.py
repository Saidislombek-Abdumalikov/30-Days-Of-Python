
#Day 1 - 30DaysOfPython Challenge BMI Calculator

weight = input("Enter weight in kg: ")

height = input("Enter height in sm: ")

weight = float(weight)
height = float(height)
height_m = height / 100

bmi = weight / (height_m ** 2)

print("Your BMI is ", bmi)
