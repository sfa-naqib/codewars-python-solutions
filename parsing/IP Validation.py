def is_valid_IP(strng):
    IP = strng.split('.')
    if len(IP) != 4:
        return False
    for i in IP:
        if not i:
            return False
        if i[0] == '0' and len(i)>1:
            return False
        if not i.isnumeric():
            return False
        if int(i) > 255:
            return False
    return True
