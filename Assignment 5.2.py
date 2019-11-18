# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

#Initialize variables
largest = None
smallest = None
n1 = []

#Function to take user input and validate the value
#Store input to list
def userinput():
    while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            n = int(num)
            n1.append(n)
        except:
            print('Invalid input')
            continue

#Function to calculate largest value in the list
def largest_number(n1, largest):
    for x in n1:
        if largest is None or x > largest :
            largest = x
    return largest

#Function to calculate smallest value in the list
def smallest_number(n1, smallest):
    for y in n1:
        if smallest is None:
            smallest = y
        elif y < smallest:
            smallest = y
    return smallest

#Invoke functions
userinput()
l = largest_number(n1, largest)
s = smallest_number(n1, smallest)

#Print output
print("Maximum is", l)
print("Minimum is", s)