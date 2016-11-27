from random import randint, sample
from itertools import chain, combinations
from time import time



class SSP():
    def __init__(self, S=[], t=0):
        """this is a dotstring - what the function does
         - what the input is
         -  what the output is
         - any assumptions etc 
         - stuff a user would find useful
         - stays in the code to help with debugging"""
        self.S = S #S is an array / list
        self.t = t # is the target 
        self.n = len(S) # is the length of the array / list 
        #
        self.decision = False # to check if the target is true ?
        self.total    = 0 # used to see if sum equals to 0
        self.selected = [] # numbers that are sum up to the target (not used)? 

    def __repr__(self): # return a printable presentation of a object
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
        #return the string instance of the object
    
    #bitlength means 2^10 which numbers 0-1024
    def random_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        #sorts the array list from largest to smallest     
        ##t is random number in the range of 0 - length of array*max_n_bit_number
        self.t = randint(0,n*max_n_bit_number)
        self.n = len( self.S )
        #

    def random_yes_instance(self, n, bitlength=10):
        #bitlength is used onmax_n_bit_number number for range, list numbers are in range of 0-1024
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        #if there is an answer for t 
        self.t = sum( sample(self.S, randint(0,n)) )
        self.n = len( self.S )

    ###
    #if target is 0 try again. 
    def try_at_random(self):
        candidate = []
        total = 0
        while total != self.t:
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )
            
#calling class and functions 
instance = SSP()
instance.random_yes_instance(4)
print( instance )

instance.try_at_random()
