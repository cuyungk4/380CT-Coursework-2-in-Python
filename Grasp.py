import random

#create a ramdom array 
def create():
      s=[]    
      for i in range (20):    
          s.append(random.randrange(1,101,1))
      s.sort(reverse=True)
      return s
#greedy algorithm
def greedy(target,list1):
      greedy_solution = []
      print list1

      for i in list1:
            if i <= target:
                  target = target - i
                  greedy_solution.append(i)
                  #print "Greedy", greedy_solution, "=", sum(greedy_solution)
      print "Greedy", greedy_solution, "=", sum(greedy_solution)
      return greedy_solution

#create RCL
def RCL(list1, greedy_solution):
      RCL = list(list1)
      for a in list1:
            if a in greedy_solution:
                  RCL.remove(a)
      #print "RCL",RCL
      return RCL
#GRASP
def grasp(target, greedy_solution, RCL, Max_Iterations):

      
      RCL = RCL
      Gsolution = greedy_solution
      t = target
      solution = list(Gsolution)
      iteration = 0
      maxt = Max_Iterations
      best = []
      new = []
      print "Solution: ", solution
      print "Gsolution: ",Gsolution
      print "RCL" , RCL
      print "Target: ",target
      Gdiff = abs(t - sum(Gsolution))
      Sdiff = 0

      
      while sum(solution) != target:

            #While total of solution is smaller than the target it will randomly select one more from RCL
            while sum(solution) < t:
            #if sum(solution) < t:
                  Rvalue = random.choice(RCL)
                  solution.append(Rvalue)
                  RCL.remove(Rvalue)
                  iteration += 1
                  print "Solution: %s = %s"%(solution,sum(solution))

      
            while sum(solution)> t:
            #if sum(solution)> t:
                  Gvalue = random.choice(solution)
                  RCL.append(Gvalue)
                  solution.remove(Gvalue)
                  iteration += 1
                  print "Solution: %s = %s"%(solution,sum(solution))
                  #print "\t\t\t\t\t\t\tnot match"

            #print "Solution: %s = %s"%(solution,sum(solution))

            #different between targe and new/best solution
            new = list(solution)
            ndiff = abs(t - sum(new))
            #print "New ",new, " " , ndiff
            odiff = abs(t - sum(best))
            #print "Best ",best, " " , odiff

            #if the new solution is have a smaller different between target, it will replace the best solution
            if ndiff<odiff:
                  best = list(new)
            elif ndiff>odiff:
                  best = list(best)
            elif ndiff == 0:
                  best = list(new)
            else:
                  best = list(new)


            if sum(solution) == t:
                  print"done"
                  break      
            '''      
            if iteration == maxt:
                  print "Over %s time of iteration, so we assume: " %iteration
                  break
            '''

      if sum(solution) != t:
            solution = best

      Sdiff = abs(sum(solution) - t)
      print "\nTarget = %s"%t
      print "Greedy" , Gsolution," = ", sum(Gsolution)
      print "GRASP soution", solution," = ", sum(solution)
      print "Iteration of GRASP :",iteration
      
      if (sum(solution)== t):
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
t = 377
s = create()
G = greedy(t,s)
R = RCL(s, G)
grasp(t, G, R, 150)

