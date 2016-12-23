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
    print "target: ", target
    startT = time.time()
    greedy(target)
    #print "%s seconds" % (time.time() - startT)
    arrTest[i] = time.time() - startT

#summing of results
sumTest = sum(arrTest)
#averaging the results
avgTest = sumTest / lenTest
print "Average time to complete ", lenTest, " algorithm runs: ", avgTest, " seconds"
#print arrTest
