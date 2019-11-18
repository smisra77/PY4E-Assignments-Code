#Program to compute gross pay with try and catch statement

#example: (40*10.50) + (5*(10.50 * 1.5)) = 498.75

#Prompt user to input hours and rate
#Assuming the user types numbers properly
hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Please enter numbers only.")
    quit()
#check if hrs > 40 and calculate gross pay
if h <= 40:
    pay = h*r
else:
    overtime = h - 40
    pay = (40 * r) + (overtime * (r * 1.5))

#Print total gross pay
print(pay)