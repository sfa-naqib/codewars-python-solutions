def digital_root(n):
    sum_d = sum(int(d) for d in str(n))
    while len(str(sum_d)) != 1:
        n = sum_d
        sum_d = sum(int(d) for d in str(n))
    return sum_d
