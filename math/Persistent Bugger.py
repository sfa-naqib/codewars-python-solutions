def persistence(n):
    # your code
    if len(str(n)) < 2:
        return 0
    digits = [int(d) for d in str(n)]
    c = 0
    
    while True:
        new_num = 1
        i = 0
        while i < len(digits):
            new_num *= digits[i]
            i += 1
        if len(str(new_num)) < 2:
            return c+1
        else:
            digits = [int(d) for d in str(new_num)]
            c += 1
