#grade checker

name = input("Student name: ")
score_M = int(input("Math score: "))
score_E = int(input("English score: "))
score_S = int(input("Science score: "))

total = score_E + score_M + score_S

print("--------- Report ---------")
print()
print("Student: ", name)
print(f"Total: {total}")
print(f'Average: {int(total / 3)}')

print()
print("Passed: ", total >= 255)
print(f"Excellent {total >= 285}")