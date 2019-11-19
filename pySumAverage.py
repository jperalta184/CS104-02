#Sum/Average Program
#Your first and last name: Jonathan Peralta
#Your student ID:s1243536

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers
#Instead of searching for a name in the list
#   Compute the sum of all 10 numbers
#   Compute the average for all 10 numbers

#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

numberlist= [20]
sumint=0
avgint=0.0
count =0
while count <20:
    numbers= float(input("Enter a number:"))
    numberlist.append(numbers)
    count+=1
for x in range (0,20):
    sumint = sumint+ numberlist[x]
print(sumint)
(avgint)=(sumint)/count
print(avgint)
