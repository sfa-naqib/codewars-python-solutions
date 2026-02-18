def max_sequence(arr):
    if not arr:
        return 0
    elif all(x<0 for x in arr):
        return 0
    elif all(x>0 for x in arr):
        return sum(arr)
    else:
        max_global = 0
        max_current = 0
        for i in arr:
            max_current = max(i,max_current+i)
            max_global = max(max_current,max_global)
        return max_global
        
