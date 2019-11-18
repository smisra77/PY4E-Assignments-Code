# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using
# the split() method. The program should build a list of words. For each word on each line check to see
# if the word is already in the list and if not append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.
#fh = romeo.txt

fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("Please re-check the filename. File doesn't exist!!!")
    quit()

lst = list()
for line in fh:
    line = line.rstrip()
    #Split line with spaces and store in words
    words = line.split()
    #Iterate each word in list and check if it alread exists in list
    #If yes, then skip else append that work to the list
    for word in words:
        if word in lst: continue
        lst.append(word)
        #sort the list in alphabetical order
        lst.sort()

print(lst)