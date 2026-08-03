#Freelancer Invoice Generator v1.2

freelancer_name = input("Freelancer name: ").strip().title()
client_name = input("Client name: ").strip().title()
client_tel = input("+998 ").strip()
invoice_id = input("Invoice ID: ").strip().upper()
invoice_month = input("Invoice month (eg.June): ").strip().lower()
project_name = input("Project name:").strip().upper()
hours_worked = int(input("Hours worked: "))
hourly_rate = int(input("Hourly rate (USD): "))
tax_ptg = int(input("Tax percentage: "))

'''FORMULA'''
total_payment = hourly_rate * hours_worked
tax_amount = total_payment / 100 * tax_ptg
final_payment = total_payment - tax_amount
payment_per_week = final_payment / 4
payment_per_day = final_payment / 30
payment_per_hour = final_payment / hours_worked

'''HEADING'''
heading_freelancer = "FREELANCER"
heading_client = "CLIENT"
heading_invoice = "INVOICE"
heading_analysis = "PAYMENT ANALYSIS"


'''PRINT'''
print("\n",heading_freelancer.center(50))

print(f"\nFreelancer Name: {freelancer_name}\n")

print("\n",heading_client.center(50))

print(f"\nClient Name: {client_name}")
print(f"Client Phone Number: +998 {client_tel}\n")

print("\n",heading_invoice.center(50))

print(f"\nInvoice ID: {invoice_id}")
print(f"Month: {invoice_month}")
print(f"Project name: {project_name}")
print(f"Hours worked: {hours_worked}")
print(f"Hourly rate: {hourly_rate} USD")
print(f"Tax percentage: {tax_ptg} %")
print(f"Tax amount: {tax_amount} USD")

print("\n",heading_analysis.center(50))

print(f"\nTotal payment: {total_payment} USD")
print(f"Final payment: {final_payment} USD")

print(f"\nPayment per")
print(f"Week: {payment_per_week:.1f} USD")
print(f"Day: {payment_per_day:.1f} USD")
print(f"Hour: {payment_per_hour:.1f}USD")