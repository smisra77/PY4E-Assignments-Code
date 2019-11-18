#Print grades using score grade

#Prompt user to enter a score
score = input("Enter Score: ")

#Check if score input is valid i.e. it's a number and within range of 0.0 - 1.0
try:
   fscore = float(score)
   if fscore >= 1.0:
       quit()
   elif fscore <= 0.0:
       quit()
except:
    print("Please enter score in numbers and withing range of 0.0 - 1.0 only.")
    quit()

#Calculate grades using valid score entered
if fscore >= 0.9:
    print('A')
elif fscore >= 0.8:
    print('B')
elif fscore >= 0.7:
    print('C')
elif fscore >= 0.6:
    print('D')
elif fscore < 0.6:
    print('F')



