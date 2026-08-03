#Freelancer Invoice Generator v1.2

freelancer_name = input("Freelancer name: ")
client_name = input("Client name: ")
client_tel = input("+998 ")
invoice_id = input("Invoice ID: ")
invoice_month = input("Invoice month (eg.June): ")
project_name = input("Project name:")
hours_worked = int(input("Hours worked: "))
hourly_rate = int(input("Hourly rate (USD): "))
tax_ptg = int(input("Tax percentage: "))

'''FORMULA'''
total_payment = hourly_rate * hours_worked
tax_amount = total_payment /100 * tax_ptg
final_pament = total_payment - tax_amount
payment_per_week = total_payment / 4
payment_per_day = total_payment / 30
payment_per_hour = total_payment / hours_worked



'''HEADING'''
heading_freelancer = "FREELANCER"
heading_client = "CLIENT"
heading_invoice = "INVOICE"
heading_analysis = "PAYMENT ANALYSIS"


'''PRINT'''
print("\n",heading_freelancer.center(50))

print(f"\nFreelancer Name: {freelancer_name.title()}\n")

print("\n",heading_client.center(50))

print(f"\nClient Name: {client_name.title()}")
print(f"Client Phone Number: +998 {client_tel}\n")

print("\n",heading_invoice.center(50))

print(f"\nInvoice ID: {invoice_id.upper()}")
print(f"Month: {invoice_month.upper()}")
print(f"Project name: {project_name.title()}")
print(f"Hours worked: {hours_worked}")
print(f"Hourly rate: {hourly_rate}USD")
print(f"Tax percentage: {tax_ptg}%")
print(f"Tax amount: {tax_amount} USD")

print("\n",heading_analysis.center(50))

print(f"\nTotal payment: {total_payment}USD")
print(f"Final payment: {final_pament}USD")

print(f"\n Payment per")
print(f"Week: {payment_per_week}")
print(f"Day: {payment_per_day}")
print(f"Hour: {payment_per_hour}\n")