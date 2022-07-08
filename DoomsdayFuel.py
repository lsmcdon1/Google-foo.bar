
import numpy as np
from numpy.linalg import inv
from fractions import Fraction as frac

def probability_matrix(lst):
    P = []
    non_absorb = []
    absorb = []
    for i in range(len(lst)):
        temp = [0] * len(lst)
        sum = 0
        for j in lst[i]: 
            sum += j

        if sum != 0: 
            non_absorb.append(i)
            for j in range(len(lst)): 
                temp[j] = lst[i][j] / sum

        elif sum == 0:
            absorb.append(i)
            temp[i] = 1.0

        P.append(temp)

    return P, non_absorb, absorb

def generate_identity(n):
    I = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j: 
                row.append(1.0)
            else: 
                row.append(0.0)
            
        I.append(row)

    return I


def format(raw_results):
    denoms = []
    for i in raw_results:
        denoms.append(i.denominator)

    denominator = 0
    for i in (range(len(denoms) - 1)):
        denominator = np.lcm(denoms[i], denoms[i+1])

    numerators = []
    for i in raw_results:
        mult = denominator / int(i.denominator)
        numerators.append(int(i.numerator * mult))

    return numerators + [int(denominator)]

def standard_form(P, non_absorb, absorb):
    order = absorb + non_absorb
    M = []
    R = []
    Q = []
    for i in range(len(P)): 
        row = []
        for j in range(len(P)):
            row.append(P[order[i]][order[j]])
        M.append(row)

    #construct matrix R
    for i in range(len(non_absorb)): 
        row = []
        for j in range(len(absorb)):
            row.append(P[non_absorb[i]][absorb[j]])
        R.append(row)

    for i in range(len(non_absorb)): 
        row = []
        for j in range(len(non_absorb)):
            row.append(P[non_absorb[i]][non_absorb[j]])
        Q.append(row)

    return np.array(M), np.array(R), np.array(Q)

def calculate_F(I, Q):
    intr = I - Q
    return inv(intr)

def solution(m):
    P, non_absorb, absorb = probability_matrix(m)
    M, R, Q = standard_form(P, non_absorb, absorb)
    I = generate_identity(len(non_absorb))
    F = calculate_F(I, Q)
    FR = (np.matmul(F, R)).tolist()

    raw_results = []
    for i in FR[0]: 
        raw_results.append(frac(i).limit_denominator())

    return format(raw_results)

soln = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
soln2 = solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])


print('done')