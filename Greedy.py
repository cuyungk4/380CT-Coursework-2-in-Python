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
def greedy(target):
    list1 = [1,2,3,4,9,10,11,12]
    solution = []
    total = 0
    #target = 0
    list1.sort(reverse=True)
    print list1

    for i in list1:
        print total
        if i <= target:
            target = target -i
            #total = total + i
            #target = target - total
            solution.append(i)
            print solution
    print sum(solution)

    
greedy(13)


