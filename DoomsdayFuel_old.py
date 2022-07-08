def row_sum(lst):
    cnt = 0
    for i in lst:
        cnt += i

    return cnt

def commonizer(lst):
    max = -1
    for i in lst: 
        if i > max: 
            max = i

    found = False
    denoms = range(max, 1, -1)

    n = 0
    while not found: 
        for i in lst:
            if i % denoms[n] == 0:
                found = True

        n += 1

    soln = [0] * len(lst)
    for i in range(len(lst)): 
        soln[i] = int(lst[i] / n)

    return soln



def solution(lst):
    n = len(lst)
    terminal_mask = [False] * n
    non_terminals = []
    terminals = []
    nonterm_sum = 0

    #figure out how many dead ends there are
    mask_id = 0
    for i in lst:
        term = True
        for j in i:
            if j != 0:
                term = False

        if term:
            terminal_mask[mask_id] = True
            terminals.append(mask_id)
        else: 
            nonterm_sum += row_sum(i)
            non_terminals.append(mask_id)

        mask_id += 1

    nonterm_sum -= row_sum(lst[0]) #we don't want to include s0 in the overall sum

    numerators = [0] * n

    #parse through s0, ore will always start here
    s0 = lst[0]
    for i in non_terminals:
        if s0[i] != 0: #don't care if 0
            for j in range(n): 
                if j != 0: #we don't want to deal with circulars yet
                    if terminal_mask[j]:
                        numerators[j] = lst[0][i] * lst[i][j]
        
    for i in terminals: 
        if s0[i] != 0: 
            numerators[i] = nonterm_sum * s0[i]
 
    denominator = 0
    soln = [0] * int(len(terminals) + 1)
    s = 0
    for i in range(n): 
        denominator += numerators[i]
        if terminal_mask[i]: 
            soln[s] = numerators[i]
            s += 1

    soln[-1] = denominator
    soln = commonizer(soln)

    return soln                    


        

    # TODO: check to see what happens if there's a circular reference (i.e. s1 -> s1)



solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])