def two_sum(numbers, target):
    for i,j in enumerate(numbers):
        complement = target - j
        try:
            dex = numbers.index(complement)
            if i != dex:
                return(i,dex)
        except:
            continue
