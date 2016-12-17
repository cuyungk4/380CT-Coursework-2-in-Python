import random
from random import randint
import copy
import time

myRandom = []
#smallest number in the list
minimum = 1
#largest number in the list
maximum = 3501
#size of the list
listSize = 150
for i in range (listSize):    
    myRandom.append(random.randrange(minimum,maximum,1))
myRandom.sort(reverse=True)
print (myRandom)
    
solution = []
target = randint(minimum, maximum)

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
    iteration = 100
    target = target
    global solution
    newSolution = copy.copy(solution)
    while iteration != 0:
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
        #else if new solution difference is smaller than old solution difference
        elif newSolDiff < oldSolDiff:
            #replace old solution with new solution
            solution = newSolution
            print "New solution: ", solution, "=", sum(solution)
            print "Keeping new solution -----------------------------"
            #decrement counter
            iteration -= 1
        #else if old solution difference is smaller than new solution difference
        elif oldSolDiff < newSolDiff:
            print "New solution: ", newSolution, "=", sum(newSolution)
            print "Discarding new solution -----------------------------"
            newSolution = copy.copy(solution)
            #print "Solution: ", newSolution, "=", sum(newSolution)
            #decrement counter
            iteration -= 1

    return newSolution, "=" ,sum(newSolution)

print "target: ", target
greedy(target)
print "-----------------------"

startT = time.time()
print iterativeImprov(target)
print "%s seconds" % (time.time() - startT)