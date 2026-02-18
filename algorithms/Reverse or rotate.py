def rev_rot(strng, sz):
    
    if sz <= 0 or strng == '' or sz > len(strng):
        return ''
    
    chunks = []
    for i in range(0,len(strng),sz):
        if i+sz <= len(strng):
            chunks.append(strng[i:i+sz])
            
    for index,chunk in enumerate(chunks):
        digits = [int(c) for c in chunk]
        if sum(digits) % 2 == 0:
            chunks[index] = chunk[::-1]
        else:
            chunks[index] = chunk[1:]+chunk[0]
    return ''.join(chunks)
