import random
import time

#create a ramdom array 
def create(n, max_n):
      stack =[]
      # n is the ammount of element
      for i in range (n):    
          stack.append(random.randrange(1,max_n,1))
      stack.sort(reverse=True)
      target = random.randrange(max_n) 
      # return the array and the target
      return stack, target
#greedy algorithm
def greedy(target,array):
      greedy_solution = []
      print array

      for i in array:
            if i <= target:
                  target = target - i
                  greedy_solution.append(i)
                  #print "Greedy", greedy_solution, "=", sum(greedy_solution)
      print "Greedy", greedy_solution, "=", sum(greedy_solution)
      return greedy_solution

#create RCL(Random Candidate List)
def RCL(array, greedy_solution):
      #make a RCL using a copy of the array
      RCL = list(array)
      #check every element in RCL, if element is in the Greedy's solution, element will be remove from RCL
      for a in RCL:
            if a in greedy_solution:
                  RCL.remove(a)
      #print "RCL",RCL
      return RCL
#GRASP
def grasp(target, greedy_solution, RCL, array, Max_Iterations):

      #slist =  array
      RCL = RCL
      Gsolution = greedy_solution
      t = target
      #let solution be copy of Greedy's solution
      solution = list(Gsolution)
      iteration = 0
      maxt = Max_Iterations
      best = []
      new = []
      #ndiff = abs(t - sum(new))
      #bdiff = abs(t - sum(best)) 
      #print "Solution: ", solution
      #print "Gsolution: ",Gsolution
      print "RCL" , RCL
      print "Target: ",target
      Gdiff = abs(t - sum(Gsolution))
      Sdiff = 0

      
      while sum(solution) != target:

            #the different between solution and targt
            diff = abs(t - sum(solution))
            #make slist as a copy of array
            slist =  list(array)
            #remove the element in slist which is already in the solution  
            for a in solution: 
                  if a in slist:
                        slist.remove(a)
            #remove the elment in the slist which is greter than the gup with the target            
            for b in slist:
                  if b > diff:
                        slist.remove(b)
                  '''
                  elif a >= diff:
                        slist.remove(a)
                  '''
            #print "\nSlist", slist
            #While total of solution is smaller than the target it will randomly select one more from RCL
            while sum(solution) < t:
            #if sum(solution) < t:
                  if len(slist) <= 0:
                        #print "There are no substring can be sum up to %s"%target
                        break
                                    
                  Rvalue = random.choice(slist)
                  #print "Rvalue" , Rvalue
                  slist.remove(Rvalue)
                  solution.append(Rvalue)
                  #print "slista" , slist
                  #print "solsutiona" , solution
                  iteration += 1
                  print "Solution: %s = %s"%(solution,sum(solution))


            while sum(solution)> t:
            #if sum(solution)> t:
                  if len(slist) <= 0:
                        #print "There are no substring can be sum up to %s"%target
                        break
                  Gvalue = random.choice(solution)
                  #print "Gvalue" , Gvalue
                  solution.remove(Gvalue)
                  slist.append(Gvalue)
                  #print "slistb" , slist
                  #print "solsutionb" , solution
                  iteration += 1
                  print "Solution: %s = %s"%(solution,sum(solution))
                  #print "\t\t\t\t\t\t\tnot match"

            #print "Final Solution: %s = %s"%(solution,sum(solution))

            
            #different between targe and new/best solution
            new = list(solution)
            ndiff = abs(t - sum(new))
            print "New ",new, " " , ndiff
            bdiff = abs(t - sum(best))
            print "Best ",best, " " , bdiff

            #if the new solution is have a smaller different between target, it will replace the best solution
            if ndiff<bdiff:
                  best = list(new)
            elif ndiff>bdiff:
                  best = list(best)
            elif ndiff == 0:
                  best = list(new)
            else:
                  best = list(new)


            if sum(best) == t:
                  print"done"
                  break
            
            elif len(slist) <= 0:
                  print "There are no substring can be sum up to %s"%target
                  break
            
            if iteration == maxt:
                  print "Over %s time of iteration, so we assume: " %iteration
                  break

      Sdiff = abs(sum(solution) - t)
      #print sorted(Gsolution+RCL),"\nThe list is above"
      print "\nThe given array :\n%s"%array
      print "Target = %s"%t
      print "Greedy" , Gsolution," = ", sum(Gsolution)
      print "GRASP soution", solution," = ", sum(solution)
      print "Iteration of GRASP :",iteration
      
      if (sum(new)== t):
            #diff =  Sdiff
            print "The best solution is GRASP which the sum is %s = %s"  %(solution, sum(solution))
      elif (Gdiff == 0):
            print "The best solution is: Greedy which the sum is %s = %s" %(Gsolution, sum(Gsolution))
      elif Gdiff> Sdiff:
            diff = Sdiff
            print "The best solution is GRASP which the sum is %s = %s" %(solution, sum(solution))
      elif Sdiff > Gdiff:
            diff = Gdiff
            print "The best solution is: Greedy which the sum is %s = %s " %(Gsolution, sum(Gsolution))

#s = [26, 24, 20, 19, 17]
#s = [7,8,2,5,6,4,9,13]
#s.sort(reverse=True)
#t = 377
            
c = create(20,101)
# array is the first element of the return value
s = c[0]
# target is the srcond element of the return value
t = c[1]
G = greedy(t,s)
R = RCL(s, G)
Tstart = time.time()
grasp(t, G, R, s, 500)
print "The algorithm finish in %s seconds."%(time.time() - Tstart)

