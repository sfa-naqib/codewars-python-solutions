def increment_string(strng):
    if not strng:
        return '1'
    elif strng[-1].isdigit() and int(strng[-1]) in range(0,9):
        strng = strng[:-1]+str(int(strng[-1])+1)
        return strng
    elif strng[-1].isdigit() and int(strng[-1]) == 9:
        num = ''
        for i in range(1,len(strng)):
            if strng[-i].isdigit():
                num += (strng[-i])
            else:
                break
        num = num[::-1]
        l = len(num)
        dig = int(num)+1
        n = ''
        for i in num:
            if i == '0':
                n += i
            else:
                break
        n += str(dig)
        if n[0] == '0' and len(n) != len(num):
            n = n[1:] 
        strng = strng[:(len(strng)-l)]+n
        return strng
    else:
        strng = strng+'1'
        return strng
        
