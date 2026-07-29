#Day 1 - 30DaysOfPython Challenge Calculator

num1 = input("Enter 1st number: ")

num2 = input("Enter 2nd number: ")

num1 = float(num1)
num2 = float(num2)

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2 
division = num1 / num2
modulus = num1 % num2
f_division = num1 // num2


exponential1 = num1 ** 2
exponential2 = num2 ** 2


print('+',addition)
print('-',subtraction)
print('/',division)
print('*',multiplication)
print('%',modulus)
print('//',f_division)



print('**',exponential1)
print('**',exponential2)

