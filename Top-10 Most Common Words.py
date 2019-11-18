#Program to calculate Top-10 most common word in a file

file = input("Enter file name: ")

try:
    fh = open(file)
except:
    print("File not found. Please re-check!!")
    quit()

db = dict()

#Create dictionary
for line in fh:
    words = line.split()
    for word in words:
        db[word] = db.get(word, 0) + 1

print('Original', db)

newlist = list()

#Create a tuple to store value first and then keys
#Append the list with these tuple
for k,v in db.items():
    newtup = (v, k)
    newlist.append(newtup)
print('newlist\n', newlist)
#Output:  [(1, 'Writing'), (2, 'programs'), (1, 'or'), (1, 'programming'), (2, 'is'), (3, 'a'), (2, 'very'),....

#Sort the newlist in deacresing order
#Used sorted
#A second important difference is that the sorted() function will return a list so you must assign the returned data to a new variable.
# The sort() function modifies the list in-place and has no return value.
#newlist = sorted(newlist, reverse=True)
newlist.sort(reverse=True)

print('Original newlist\n', newlist)
#[(16, 'to'), (6, 'the'), (5, 'we'), (5, 'our'), (5, 'of'), (5, 'do'), (5, 'computers'),.....

#Slicing to extract only first 10 values from the list 0-9 count
for v, k in newlist[:10]:
    print(k , v)