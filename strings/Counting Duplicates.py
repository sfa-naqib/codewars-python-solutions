def duplicate_count(text):
    # Your code goes here
    set_text = set(i for i in text.lower())
    count = 0
    
    for i in set_text:
        if text.lower().count(i)>1:
            count += 1
    
    return count
