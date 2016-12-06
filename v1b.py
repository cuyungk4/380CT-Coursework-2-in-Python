import math
from random import random

def powersert (items):
      res = [[]]
      for item in items:
            newset = [r+[item] for r in res]
            res.extend(newset)
      return res

def display( stack ,target):
      s = stack
      t = target
      print "data" ,s
      for a in range (len(powersert(s))):
            line = (powersert(s))[a]
            total= sum((powersert(s))[a])
            print "substring %s  Total: %s"%(line,total)
            if (total == target):
                  print "\n\nThe anawers is below: "
                  print "substring %s  Total: %s"%(line,total)
                  break
      print"None of subset total is: %s"%target 



s = [12, 24, 52, 90, 56, 23, 10]
t = 134
display(s,t)
            
     


