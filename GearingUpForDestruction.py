import numpy as np 
from fractions import Fraction

def check(soln): # Used to check if LinAlg produced a valid result (all postive vals greater than 1)
    for n in soln: 
        if n < 1.0: 
            return False

    return True

def solution(p):
    l = len(p) #number of pegs in use
    d = [0] * l #list to track distance between pegs
    
    for n in range(0, l-1): 
        d[n] = p[n+1] - p[n] #calculates the distance between pegs
        
    #init blank matrices for system of equations  
    A = [] 
    b = []
    
    # We need to make a system of equations that we can solve to determine the radius of each gear
    # So, if there are three gears with radaii x, y, z, the equations would look as follows: 
        # x + y = d0
        # y + z = d1
        # -x + 2z = 0  // this equation is used to bind via the overall gear ratio

    for n in range(0, l-1): 
        temp = [0] * l
        temp[n] = 1.0
        temp[n+1] = 1.0
        
        A.append(temp)
        b.append(float(d[n]))

    temp = [0] * l
    temp[0] = -1.0
    temp[-1] = 2.0
    A.append(temp)
    b.append(0.0)

    #use Numpy linalg to solve the system of equations
    soln = np.linalg.solve(A, b)
    
    #check the solution, format result as a fraction
    if check(soln): 
        frack = Fraction(soln[0]).limit_denominator()
        return frack.numerator, frack.denominator
    else: 
        return [-1, -1] #default return if non-valid solution found