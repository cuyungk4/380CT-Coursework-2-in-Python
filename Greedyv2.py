import random
from random import randint
import time

def create(listSize, min_d, max_d):
    myRandom = []
    minimum = min_d
    maximum = max_d
    # n is the amount of element
    for i in range (listSize):
        myRandom.append(random.randrange(minimum,maximum,1))
    myRandom.sort(reverse=True)
    print (myRandom)
    #create a random number for target
    target = random.randrange(max_d*(len(str(max_d)))) 
    # return the array and the target
    return myRandom, target

'''
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
'''

def greedy():
    c = create(10,0,100)
    #list1 = [1,2,3,4,9,10,11,12]
    myRandom = c[0]
    print "Given list: ",myRandom
    solution = []
    total = 0
    #getting target
    target = c[1]
    print "Target: ",target
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
    if len(solution) == 0:
        print "Greedy can be appply, because the target is too small"

####test variables####
#length of test; run the test ___ times
lenTest = 5
#list containng test execution time results
arrTest = [0] * lenTest
#average variable
avgTest = 0
#sum of list
sumTest = 0
####test variables####

#test loop
for i in range(0, lenTest, 1):
    print "\nTest No.",i
    startT = time.time()
    greedy()
    #print "%s seconds" % (time.time() - startT)
    arrTest[i] = time.time() - startT

#summing of results
sumTest = sum(arrTest)
#averaging the results
avgTest = sumTest / lenTest
print "\nAverage time to complete ", lenTest, " algorithm runs: ", avgTest, " seconds"
#print arrTest
