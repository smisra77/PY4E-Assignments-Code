#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print("Please re-check the filename. File doesn't exist!!!")
    quit()

db = dict()

#Read through file
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
# Gaurdian checking that line should have minimum 2 words
    if len(line) < 2: continue
#Split line on white-spaces
    words = line.split()
#Extract 2nd word in list
    email = words[1]
#Contruct dictionary using email as key
    db[email] = db.get(email, 0) + 1

maxemail = None #key
maxcount = None #value

#Calculate the most prolific committer
for k, v in db.items():
    if maxcount is None or v > maxcount:
        maxcount = v
        maxemail = k

print(maxemail,maxcount)


