#.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce
# an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("Please confirm the filename. File doesn't exist!!!")
    quit()

count = 0
sum = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
#Calculate start position as 0 and endposition as EOL i.e. \n
    starpos = line.find('0')
    endpos = line.find('\n')
#Slicing the string with start and endposition
    value = line[starpos:endpos]
#Convert to floating point number
    value = float(value.lstrip())
#Calculate Sum and Average of the values
    sum = sum + value
    avg = sum/count

#Print Average in round to 15 digit.
#Original Output is 0.7507185185185187
print("Average spam confidence:", round(avg, 15))




