import random

list1 = []

#list of length 500 random numbers between 99 and 999
for i in range(0,500):
    list1.append(random.randint(99,999))
print list1
print " "

def hillClimb(target):
    print "Target value: ", target
    #pick random number for total (can be done with the solution given by Greedy)
    total = list1[random.randint(0,50)]
    #recording the index
    index = list1.index(total)
    print "Start total: ", total
    print "Start index: ", index
    print " "

    if total == target:
        return True
    #while the total is not equal to the target
    while total != target:
        tempTotal = list1[index+1] + total
        #if total is larger than the target
        if total > target:
            #checks previous total and current total
            prevDiff = target - oldTotal
            curDiff = abs(target - total)
            #if difference between previous total and target is smaller, pick previous
            if prevDiff < curDiff:
                print "Closest sum: ", oldTotal
                print "(Absolute difference of current total and target: ", curDiff, ")"
                print "(Absolute difference of previous total and target: ", prevDiff, ")"
            #else difference between current total and target is smaller, pick current
            else:
                print "Closest sum: ", total
                print "(Absolute difference of current total and target: ", curDiff, ")"
                print "(Absolute difference of previous total and target: ", prevDiff, ")"
            return False
        #if total is less than previous total
        if total < tempTotal:
            oldTotal = total
            total = tempTotal
            index = index + 1
            print total, ",index: ", index - 1

    
        
print hillClimb(1435)
