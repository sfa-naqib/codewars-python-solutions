def sort_array(source_array):
    
    sorted_odd = sorted([y for y in source_array if y % 2 == 1])
    
    i = 0
    for index,value in enumerate(source_array):
        if value % 2 == 0:
            continue
        else:
            source_array[index] = sorted_odd[i]
            i+=1
    return source_array
