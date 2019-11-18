#Program to input file name
#find largest word occurrence in text
#print count and word

file = input("Enter file name: ")

try:
    fh = open(file)
except:
    print("File not found. Please re-check!!")
    quit()

db = dict()
#Iterate through file and create a list with all words line by line
for line in fh:
    words = line.split()
    for word in words:
        #Building dictionary
        db[word] = db.get(word, 0) + 1

#Line 19 is same as below:
#if key in db:
#    db[key] = db[key] + 1
#else:
#    db[key] = 1

print('Words and its counts\n', db)

#Find largest occurrence of word and it's count
bigcount = None #value
bigword = None  #key

for k, v in db.items(): #To iterate every key and value in dictionary
    if bigcount is None or v > bigcount:
        bigword = k
#        print(bigword)
        bigcount = v

print('\nMost Frequent Word:', bigword, '\nHighest Count:', bigcount)

