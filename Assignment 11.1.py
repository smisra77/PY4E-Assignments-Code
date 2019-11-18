# Read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

file = input("Enter the filename: ")
try:
    fh = open(file)
except:
    print("Please check the filename!!!")
    quit()

lst = list()
sum = 0

for line in fh:
    line = line.rstrip()
#Read through the line and extract one or more occurrence of number between 0 to 9
    y = re.findall('[0-9]+', line)
#Extend each value extracted to a list
    lst.extend(y)

print('orignal\n',lst)

#Calculate the sum of elements in the list
for num in lst:
    sum += int(num)

print(sum)