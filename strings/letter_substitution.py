def rot13(message):
    m = ''
    for i in message:
        if not i.isalpha():
            m += i
        else:
            if ord(i) in range(65,78) or ord(i) in range(97,110):
                m += chr(ord(i)+13)
            else:
                m += chr(ord(i)-13)
    return m
        
