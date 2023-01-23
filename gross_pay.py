#the programme calculates the gross pay of an employee

def gross_pay(hours_worked, rate_per_hour): #The def is used as a function
    
        return (hours_worked * rate_per_hour)

hours_worked = int(input("Enter hours worked:"))
rate_per_hour = float(input("Enter rate per hour:"))

gross_pay = hours_worked*rate_per_hour
 
print("Total gross pay: ",gross_pay)