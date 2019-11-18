# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

# Use words.txt as the file name
fname = input("Enter file name: ")

#Validate if file exists in directory
try:
    fh = open(fname)
except:
    print("File name does not exist!!!")
    quit()

#Function to change file content to upper case
def upper_case(fh):
    for line in fh:
        line = line.rstrip()
        line = line.upper()
        print(line)

#Invoke funtion
upper_case(fh)