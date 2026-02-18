def create_phone_number(n):
    #your code here
    ns = [str(x) for x in n]
    return f"({''.join(ns[:3])}) {''.join(ns[3:6])}-{''.join(ns[6:])}"
