def stock_list(stocklist, categories):
    # your code here
    if not stocklist:
        return ''
    categories_dict = {letter: 0 for letter in categories}
    
    for item in stocklist:
        cat = item.split()[0][0]
        value = int(item.split()[1])
        if cat in categories_dict.keys():
            categories_dict[cat] += value
    
    string = ''
    for key,value in categories_dict.items():
        string += f'({key} : {value}) - '
    return string[:-3]
        
