'''
Works by taking the highest number every time until it hits the target

example:
[1,2,3,4,5,6,7]
target = 21
21 - 7 = 14
                [7]
14 - 6 = 8
                [7, 6]
8 - 5 = 3
                [7, 6, 5]
3 - 3 = 0
                [7, 6, 5, 3]
TARGET MET

'''
import random
from random import randint
import time

myRandom = []
#smallest number in the list
minimum = 1
#largest number in the list
maximum = 101
#size of the list
listSize = 20
for i in range (listSize):    
    myRandom.append(random.randrange(minimum,maximum,1))
myRandom.sort(reverse=True)
print (myRandom)

target = randint(minimum, maximum)

def greedy(target):
    #list1 = [1,2,3,4,9,10,11,12]
    solution = []
    total = 0
    #target = 0
    #list1.sort(reverse=True)
    #print list1

    for i in myRandom:
        #print total
        if i <= target:
            target = target -i
            #total = total + i
            #target = target - total
            solution.append(i)
            print solution, "=", sum(solution)

print "target: ", target
startT = time.time()
greedy(target)
print "%s seconds" % (time.time() - startT)
