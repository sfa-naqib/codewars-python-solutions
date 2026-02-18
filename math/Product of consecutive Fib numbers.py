def product_fib(_prod):
    f = [0,1]
    for i in range(2,1000): 
        f.append(f[i-1]+f[i-2])
    for i in range(999):
        if f[i]*f[i+1] == _prod:
            return [f[i],f[i+1],True]
    for i in range(999):
        if f[i]*f[i+1] > _prod:
            return [f[i],f[i+1],False]
