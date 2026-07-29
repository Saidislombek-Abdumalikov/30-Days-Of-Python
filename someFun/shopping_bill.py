#shopping bill

pd1 = int(input("Product 1 price: "))
pd2 = int(input("Product 2 price: "))
pd3 = int(input("Product 3 price: "))

total = pd1 + pd2 + pd3
average = total / 3

print()

print("--------- Receipt -------")

print()

print(f"Total: {total}")
print(f"Average price: {average}")