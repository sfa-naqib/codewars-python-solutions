def find_outlier(integers):
    even = list(filter(lambda x: x%2 == 0,integers))
    odd = list(filter(lambda x: x%2 == 1,integers))
    if(len(even) == 1):
        return(even[0])
    else:
        return(odd[0])
