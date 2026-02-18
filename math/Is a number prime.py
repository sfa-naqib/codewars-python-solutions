from math import sqrt
def is_prime(num):
    if num < 2:
        return False
    if num in (2,3):
        return True
    if num % 2 == 0:
        return False
    factors = []
    for i in range(3,int(sqrt(num))+1,2):
        if num % i == 0:
            factors.append(i)
    return len(factors) == 0
