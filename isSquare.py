import math
def is_square(n):
    if n < 0:      
        return False
    if n == 0:    
        return True
    else:
        sqr = math.sqrt(n)
        return int(sqr + 0.5) ** 2 == n