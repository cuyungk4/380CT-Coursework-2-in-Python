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
my_randoms=[]    
for i in range (20):    
    my_randoms.append(random.randrange(1,101,1))
my_randoms.sort(reverse=True)
print (my_randoms)
    

def greedy(target):
    #list1 = [1,2,3,4,9,10,11,12]
    solution = []
    total = 0
    #target = 0
    #list1.sort(reverse=True)
    #print list1

    for i in my_randoms:
        #print total
        if i <= target:
            target = target -i
            #total = total + i
            #target = target - total
            solution.append(i)
            print solution, "=", sum(solution)

    
greedy(326)

