#Program to read a text file and parse each word.
#Sort the list by length of each word in descending order
#If words length is same, then sort by alphabetical order i.e. what, soft

file = input("Enter a filename? ")

try:
    fh = open(file)
except:
    print("File not found!!!")
    quit()

db1 = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        lenofword = len(word)
        # sort works on only 'key', not 'values'. So reversed in newtup
        newtup = (lenofword, word)
        db1.append(newtup) #It can take only one arguments

#why not used dictionary?
# Because this is not itterrable elements. Only one occurrence. Just counting length.
#Example w/o dictionary: (9, 'computers'), (9, 'computers'), (9, 'computers'), (9, 'computers'), (9, 'computers'),

print('DB1 = ', db1)

db1.sort(reverse=True)

print('Reversed DB1 = ', db1)

#this is just to print only words, but not it's length
db2 = list()

for l, w in db1:
    db2.append(w)

print('Reversed words list = ', db2)

