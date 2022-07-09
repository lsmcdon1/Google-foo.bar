def solution(x, y):
    x = int(x)
    y = int(y)
    if x == 1 and y == 1: 
        return "0"
    elif x == y: 
        return "impossible" 
    
    iterations = 0
    
    while not found: 
        if x < 1 or y < 1: 
            return 'impossible'
            
        elif x == 1 and y == 1: 
            return str(iterations)
            
        elif x == y:
            return 'impossible'
            
        else: 
            mult =  int((max(x, y) - 1)/min(x, y))
            x, y = max(x, y) - (min(x, y) * mult), min(x, y)
            iterations += 1 * mult
            

                
one = solution('9', '2')
two = solution('9', '1')


'halt' #attach debugger to prevent loop out