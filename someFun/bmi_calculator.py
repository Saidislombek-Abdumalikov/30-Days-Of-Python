#bmi calculator

weight = int(input("Enter your weight (kg): "))
height = int(input("Enter your height (cm): "))

height_m = height / 100
bmi = weight / height_m ** 2

print(bmi)


