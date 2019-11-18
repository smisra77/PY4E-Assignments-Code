#Program to compute gross pay

#example: (40*10.50) + (5*(10.50 * 1.5)) = 498.75

#Prompt user to input hours and rate
#Assuming the user types numbers properly
hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

#check if hrs > 40 and calculate gross pay
if h <= 40:
    pay = h*r
else:
    overtime = h - 40
    pay = (40 * r) + (overtime * (r * 1.5))

#Print total gross pay
print(pay)