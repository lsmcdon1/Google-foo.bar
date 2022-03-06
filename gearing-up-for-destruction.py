import numpy as np
from fractions import Fraction

def check(soln): 
    for n in soln: 
        if n < 1.0: 
            return False

    return True

def solution(p):
    l = len(p)
    d = [0] * l
    
    for n in range(0, l-1): 
        d[n] = p[n+1] - p[n]
        
    A = []
    b = []
    
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


    
    soln = np.linalg.solve(A, b)
    print(check(soln))
    if check(soln): 
        frack = Fraction(soln[0]).limit_denominator()
        return frack.numerator, frack.denominator
    else: 
        return [-1, -1]

print(solution([4, 30, 50]))