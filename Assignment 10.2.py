#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
# a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print("File not found!!!")
    quit()

db = dict()
newlist = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
#    print('words: ',words)
#    words = ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
    # Gaurdian checking for minimum length to include timestamp
    if len(words) < 6: continue
    time = words[5]
#    print('time: ', time)
    time = time.split(':')
    hour = time[0]
#    print('hour: ', hour)
# Create dictionary with 'hour' as 'key' and 'value' as occurrence.
    db[hour] = db.get(hour, 0) + 1

#print('db: ', db)

#Changing to dictionary to list and append values
for k, v in list(db.items()):
#build list of tuples
    newlist.append((k,v))

#Sort the list by hour in ascending order
newlist = sorted(newlist)

#Print all values
for k,v in newlist:
    print(k,v)