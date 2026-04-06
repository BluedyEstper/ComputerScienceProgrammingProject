# main.py
# Simple Python starter script.

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
    job_position=input("Enter the job position of " + name + ": ")
    hours_worked=int(input("Enter the hours worked by " + name + ": "))
    worker.append(name)
    worker.append(job_position)
    worker.append(hours_worked) 
    database.append(worker) 

for i in range(3):
    print("\nEntering data for worker...")
    worker_info()
# range is simplified to 3 for testing purposes, change to 10 for actual use

print(database)
