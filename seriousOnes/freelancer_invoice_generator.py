#Freelancer Invoice Generator

freelancer_name = input("Freelancer name: ")
client_name = input("Client name: ")
client_tel = int(input("+998 "))
invoice_id = input("Invoice ID: ")
invoice_month = input("Invoice month (eg.June): ")
project_name = input("Project name:")
hours_worked = int(input("Hours woked: "))
hourly_rate = int(input("Hourly rate (USD): "))

total_payment = hourly_rate * hours_worked

print("\nFREELANCER".center(50))

print(f"\nFreelancer Name: {freelancer_name}\n")

print("\nCLIENT".center(50))

print(f"\nClient Name: {client_name}")
print(f"Client Phone Number: {client_tel}\n")

print("\nINVOICE".center(50))

print(f"\nInvoice ID: {invoice_id}")
print(f"Month: {invoice_month}")
print(f"Project name: {project_name}")
print(f"Hours worked: {hours_worked}")
print(f"Hourly rate: {hourly_rate}")
print(f"Total payment: {total_payment}")

