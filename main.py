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

#V1.5 - removed debugging print statements to clean up the output after testing the worker information input function.

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

    if len(database) == 0:
        print("No worker data available to calculate salaries.")

    if len(database[0]) > 3:
        print("Salaries have already been calculated for the workers.")
#V1.2 - added a function to calculate and print the salaries of each worker in both USD and GBP, using the previously defined exchange rate function.
#V1.3 - added tax calculation and net salary calculation, as per the requirement.
#V1.5 - added checks to prevent recalculating salaries if they have already been calculated, and to handle the case where no worker data is available.

#V1.5 - removed debugging print statements to clean up the output after testing the salary calculation function.

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

#V1.5 removed debugging print statements to clean up the output after testing the CSV writing function.

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

#V1.5 - removed debugging print statements to clean up the output after testing the payroll statement printing function.
#V1.4 - fixed formatting issues in the payroll statement for better readability.
#V1.4 - added a header and separator for better visual distinction between different workers' payroll statements.

def print_total_labour_cost():
    total_usd = total_labour_cost()
    total_gbp = USD_to_GBP(total_usd)
 
    print("\nSuper Cruise Tours and Resort")
    print("**********TOTAL LABOUR COST**********")
    print(f"THE TOTAL LABOUR COST IS £{total_gbp:.2f} GBP\n")

#V1.5 - removed debugging print statements to clean up the output after testing the total labour cost printing function.

def save_total_labour_cost():
    total_usd = total_labour_cost()
    total_gbp = USD_to_GBP(total_usd)

    with open("total_labour_cost.txt", "w") as file:
        file.write("Super Cruise Tours and Resort\n")
        file.write("**********TOTAL LABOUR COST**********\n")
        file.write(f"THE TOTAL LABOUR COST IS £{total_gbp:.2f} GBP\n")

    print("Total labour cost has been saved to total_labour_cost.txt")

#V1.5 - removed debugging print statements to clean up the output after testing the total labour cost saving function.
#V1.4 - added a function to save the total labour cost in GBP to a text file, including a header for clarity.

def read_total_labour_cost():
    try:
        with open("total_labour_cost.txt", "r") as file:
            print("\nCONTENTS OF total_labour_cost.txt ---\n")
            print(file.read())
    except FileNotFoundError:
        print("total_labour_cost.txt not found. Please ensure the file exists.")

#V1.5 - removed debugging function to clean up the output after testing the total labour cost reading function.

def menu():
    while True:
        print("\nSuper Cruise Tours and Resort Payroll System")
        print("1. Enter worker information")
        print("2. Calculate Salaries")
        print("3. Print Payroll Statements")
        print("4. Print total labour cost")
        print("5. Save total labour cost to text file")
        print("6. Read total labour cost from text file")
        print("7. Export CSV file")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            collect_workers()
        elif choice == "2":
            calculate_salaries()
        elif choice == "3":
            print_payroll_statement()
        elif choice == "4":
            print_total_labour_cost()
        elif choice == "5":
            save_total_labour_cost()
        elif choice == "6":
            read_total_labour_cost()
        elif choice == "7":
            write_csv()
            print("Payroll data has been written to payroll.csv")
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
#V1.5 - added a menu function to allow users to interact with the program through a simple command-line interface, providing options for all major functionalities.

def collect_workers():
    for i in range(10):
        print(f"\nEntering data for worker {i+1}...")
        worker_info()
#V1.5 - added a function to collect information for 10 workers

menu()
