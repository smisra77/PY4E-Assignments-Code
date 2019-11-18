#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.

#input rate/hour and hours
hrs = input("Enter hours: ")
rate = input("Enter rates: ")

#convert string type to float
float_rate = float(rate)
float_hrs = float(hrs)

#calculat pay
pay = float_rate * float_hrs
print("Pay:",pay)
