#student report card

#difficulty ****

print("----- Student Info -----")
print()

s_name = input("Student name: ")
print()

print("----- Subject Marks -----")
print()

math_mark = int(input("Math score (100): "))
english_mark = int(input("English score (100): "))
science_mark = int(input("Science score (100): "))
history_mark = int(input("History score (100): "))

total_marks = math_mark + english_mark + science_mark + history_mark
highest_mark = 4 * 100
avg_mark = total_marks / 4
percentage_mark = total_marks * 100 / highest_mark
lost_mark = highest_mark - total_marks

print()
print("------- STUDENT REPORT CARD --------")
print()

print(f"Student Name: {s_name}")
print()

print("Subjects")
print(f"Math: {math_mark}")
print(f"English: {english_mark}")
print(f"Science: {science_mark}")
print(f"History: {history_mark}")
print()

print("---------------------------------")
print()

print(f"Total Marks: {total_marks}")
print()

print(f"Highest Possible Marks: {highest_mark}")
print()

print(f"Percentage Marks: {percentage_mark} %")
print()

print(f"Average Marks: {avg_mark}")
print()

print(f"Marks Lost: {lost_mark}" )
print()

print("===================================")