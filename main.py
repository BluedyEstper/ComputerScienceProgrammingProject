# main.py
# Simple Python starter script.

#V1.2 - added a function to convert USD to GBP, as per the requirement.

def USD_to_GBP(amount):
    # exchange rates
    GBP = amount / 1.33 
    return GBP

# database 2D array startup
database = []

# layout of the database will be:
# [name, job_position, hours worked]
# job positions and their hourly rates:
# Front Desk - $14 USD per hour
# Kitchen - $16 USD per hour
# House Keeping - $15 USD per hour
# Maintenance - $20 USD per hour
# remember workers must work at least 100 hours per month

# code should ask for the names, job positions, and hours worked for 10 workers
# use a function to have the database ready first
# remember you have to define a function first before you can call it

def worker_info():
    worker=[]
    name=input("Enter full name of the worker: ")

    job_position=input("Enter the job position of " + name + ": ").lower().strip()
    valid_positions = ["front desk", "kitchen", "house keeping", "maintenance"]
    while job_position not in valid_positions:
        print("Invalid job position. Please enter one of the following: ", valid_positions)
        job_position=input("Enter the job position of " + name + ": ").lower().strip()
    
    hours_worked=int(input("Enter the hours worked by " + name + ": "))
    while hours_worked < 100:
        print(name, "has not worked the minimum 100 hours.")
        hours_worked=int(input("please re-enter the hours worked by " + name + ": "))
    
    worker.append(name)
    worker.append(job_position)
    worker.append(hours_worked) 
    database.append(worker) 

#V1.2 - added a while loop to ensure that the hours worked is at least 100, as per the requirement.
#V1.2 - added a while loop to validate the job position input, ensuring it matches one of the predefined valid positions.

for i in range(3):
    print("\nEntering data for worker...")
    worker_info()
# range is simplified to 3 for testing purposes, change to 10 for actual use

print(database)
# debugging print statement to check the initial database structure after collecting worker information.

salary_rates = {
    "front desk": 14,
    "kitchen": 16,
    "house keeping": 15,
    "maintenance": 20
}
#V1.2 - added a dictionary to store the hourly rates for each job position, making it easier to calculate salaries later on.

def calculate_salaries():
    for worker in database:
        name = worker[0]
        job_position = worker[1]
        hours_worked = worker[2]
        hourly_rate = salary_rates[job_position]
        gross_usd = hourly_rate * hours_worked
        gross_gbp = USD_to_GBP(gross_usd)
        tax_gbp = gross_gbp * 0.15
        net_gbp = gross_gbp - tax_gbp
        worker.append(hourly_rate)
        worker.append(gross_usd)
        worker.append(gross_gbp)
        worker.append(tax_gbp)
        worker.append(net_gbp)
        print(f"{name} earns ${gross_usd:.2f} USD, which is £{gross_gbp:.2f} GBP before tax. After a 15% tax deduction (£{tax_gbp:.2f}), the net salary is £{net_gbp:.2f} GBP.")
#V1.2 - added a function to calculate and print the salaries of each worker in both USD and GBP, using the previously defined exchange rate function.
#V1.3 - added tax calculation and net salary calculation, as per the requirement.

calculate_salaries()
print(database)
# debugging print statement to check the updated database structure after salary calculations.

# current database structure at this moment:
# [0] name
# [1] job_position
# [2] hours_worked
# [3] hourly_rate
# [4] gross_usd
# [5] gross_gbp
# [6] tax_gbp
# [7] net_gbp

def total_labour_cost():
    total = 0
    for worker in database:
        gross_usd = worker[4]
        total += gross_usd
    return total
print("The Total labour cost in USD Super Cruise Tours and Resort will have to pay out this month is: $", total_labour_cost())
#V1.3 - added a function to calculate the total labour cost in USD by summing up the gross salaries of all workers.

import csv
def write_csv():
    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "name",
            "job_position",
            "hours_worked",
            "hourly_rate",
            "gross_usd",
            "gross_gbp",
            "tax_gbp",
            "net_gbp"
        ])

        for worker in database:
            writer.writerow(worker)
#V1.3 - added a function to write the payroll data to a CSV file, including headers for clarity.
#V1.3 - fixed the CSV writing function to ensure it writes the correct data structure to the file.

write_csv()
print("Payroll data has been written to payroll.csv")
#V1.3 - added a print statement to confirm that the payroll data has been successfully written to the CSV file.

def print_payroll_statement():
    for worker in database:
        name = worker[0]
        job_position = worker[1]
        gross_usd = worker[4]
        gross_gbp = worker[5]
        tax_gbp = worker[6]
        net_gbp = worker[7]

        print("\nSuper Cruise Tours and Resort")
        print("**********MONTHLY PAYROLL STATEMENT**********")
        print(f"NAME: {name}")
        print(f"JOB POSITION: {job_position}")
        print(f"GROSS INCOME (USD): ${gross_usd:.2f}")
        print(f"GROSS INCOME (GBP): £{gross_gbp:.2f}")
        print(f"TAX (GBP): £{tax_gbp:.2f}")
        print(f"NET INCOME (GBP): £{net_gbp:.2f}")
        print("\n------------------------------------------------\n")

print_payroll_statement()
#V1.4 - added a function to print a formatted payroll statement for each worker, including all relevant salary details in both USD and GBP.
#V1.4 - fixed formatting issues in the payroll statement for better readability.
#V1.4 - added a header and separator for better visual distinction between different workers' payroll statements.

def print_total_labour_cost():
    total_usd = total_labour_cost()
    total_gbp = USD_to_GBP(total_usd)
 
    print("\nSuper Cruise Tours and Resort")
    print("**********TOTAL LABOUR COST**********")
    print(f"THE TOTAL LABOUR COST IS £{total_gbp:.2f} GBP\n")

print_total_labour_cost()
#V1.4 - added a function to print the total labour cost in GBP, using the previously defined total_labour_cost function and the USD_to_GBP conversion function.

def save_total_labour_cost():
    total_usd = total_labour_cost()
    total_gbp = USD_to_GBP(total_usd)

    with open("total_labour_cost.txt", "w") as file:
        file.write("Super Cruise Tours and Resort\n")
        file.write("**********TOTAL LABOUR COST**********\n")
        file.write(f"THE TOTAL LABOUR COST IS £{total_gbp:.2f} GBP\n")

    print("Total labour cost has been saved to total_labour_cost.txt")

save_total_labour_cost()
#V1.4 - added a function to save the total labour cost in GBP to a text file, including a header for clarity.

def read_total_labour_cost():
    try:
        with open("total_labour_cost.txt", "r") as file:
            print("\nCONTENTS OF total_labour_cost.txt ---\n")
            print(file.read())
    except FileNotFoundError:
        print("total_labour_cost.txt not found. Please ensure the file exists.")

read_total_labour_cost()
#V1.4 - added a function to read and print the contents of the total_labour_cost.txt file, with error handling for file not found.
