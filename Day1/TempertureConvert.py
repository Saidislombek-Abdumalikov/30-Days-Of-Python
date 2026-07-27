
#Day 1 - 30DaysOfPython Challenge Temperature Converter

C = input("Enter the Celcius: ")
F = input("Enter the Fahrenheit: ")

C = float(C)
F = float(F)

C_F = C * 9/5 + 32
F_C = (F - 32) * 5/9

print("Celsius → Fahrenheit", C_F)
print("Fahrenheit → Celsius", F_C)