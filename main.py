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
        salary = hourly_rate * hours_worked
        print(f"{name} earns ${salary} USD, which is £{USD_to_GBP(salary):.2f} GBP.")
#V1.2 - added a function to calculate and print the salaries of each worker in both USD and GBP, using the previously defined exchange rate function.

calculate_salaries()