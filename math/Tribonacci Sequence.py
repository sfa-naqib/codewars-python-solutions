def tribonacci(signature, n):
    if n == 0 :
        return([])
    elif n <3:
        return(signature[:n])
    else:
        for i in range(n-3):
            signature.append(signature[i] + signature[i+1] + signature[i+2])
        return(signature)
