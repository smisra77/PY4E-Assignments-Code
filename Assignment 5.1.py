#Program to repeatedly read numbers until user enters "done".

count = 0
total = 0

while True:
    line = input("Enter a number: ")
    if line == 'done':
        break
        quit()
    try:
        iline = int(line)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + iline
print(total, count, total/count)
