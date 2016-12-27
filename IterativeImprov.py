import random
from random import randint
import copy
import time

def greedy(target):
    #solution = []
    total = 0

    for i in myRandom:
        #print total
        if i <= target:
            target = target -i
            solution.append(i)
            print solution, "=", sum(solution)
    return solution 



def iterativeImprov(target):
    iteration = 10
    counter = 0
    target = target
    global solution
    newSolution = copy.copy(solution)
    while solution != target:
        #if list is empty, stop
        if not solution:
            print "empty list"
            break
        #pick a random number in solution and replace it with a
        #random number in myRandom
        index = solution.index(random.choice(solution))
        newSolution[index] = random.choice(myRandom)
        '''
        uncomment to see index and numbers being replaced
        print "index:", index, ",", newSolution[index]
        '''
        #working out the differences
        oldSolDiff = abs(target - sum(solution))
        newSolDiff = abs(target - sum(newSolution))
        #if target is met
        if target == sum(solution):
            return "Target met", solution ,"=", sum(solution)
        
        elif counter == iteration:
            print "Reached %s iterations, stopping execution" %iteration
            break
        #else if new solution difference is smaller than old solution difference
        elif newSolDiff < oldSolDiff:
            #replace old solution with new solution
            solution = newSolution
            print "New solution: ", solution, "=", sum(solution)
            print "Keeping new solution -----------------------------"
            #decrement counter
            counter += 1
        #else if old solution difference is smaller than new solution difference
        elif oldSolDiff < newSolDiff:
            print "New solution: ", newSolution, "=", sum(newSolution)
            print "Discarding new solution -----------------------------"
            newSolution = copy.copy(solution)
            #print "Solution: ", newSolution, "=", sum(newSolution)
            #decrement counter
            counter += 1

    return newSolution, "=" ,sum(newSolution), "iteration: ", counter



####test variables####
#length of test; run the test ___ times
lenTest = 100
#list containng test execution time results
arrTest = [0] * lenTest
#average variable
avgTest = 0
#sum of list
sumTest = 0
####test variables####

#test loop
for i in range(0, lenTest, 1):
    myRandom = []
    #smallest number in the list
    minimum = 1
    #largest number in the list
    maximum = 10
    #size of the list
    listSize = 10
    for i in range (listSize):    
        myRandom.append(random.randrange(minimum,maximum,1))
    myRandom.sort(reverse=True)
    print (myRandom)
        
    solution = []
    #randomising target
    target = randint(minimum, maximum)

    print "target: ", target
    greedy(target)
    print "-----------------------"
    
    startT = time.time()
    print iterativeImprov(target)
    #print "%s seconds" % (time.time() - startT)
    arrTest[i] = time.time() - startT

#summing of results
sumTest = sum(arrTest)
#averaging the results
avgTest = sumTest / lenTest
print "Average time to complete ", lenTest, " algorithm runs: ", avgTest, " seconds"
#print arrTest

'''startT = time.time()
print iterativeImprov(target)
print "%s seconds" % (time.time() - startT)'''
