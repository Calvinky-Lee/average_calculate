totalSum = int(0)
numberofNumbers = int(0)
nextNum = int(input("enter in numbers: \n"))

while (nextNum != 0):
    totalSum += nextNum
    numberofNumbers += 1
    nextNum = int(input(""))

if nextNum == 0:
    totalSum = totalSum / numberofNumbers
    print(totalSum)    
