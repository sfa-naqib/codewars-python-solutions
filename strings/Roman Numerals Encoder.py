def solution(n):
    # TODO convert int to roman string
    roman_dict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
    roman_dict = dict(reversed(list(roman_dict.items())))
    roman_code = ''
    
    for i,j in roman_dict.items():
        if n >= i and (n // i):
            roman_code += roman_dict[i] * (n // i)
            n -= i * (n // i)
            
    roman_code = roman_code.replace('VIIII','IX')
    roman_code = roman_code.replace('LXXXX','XC')
    roman_code = roman_code.replace('DCCCC','CM')
    roman_code = roman_code.replace('IIII','IV')
    roman_code = roman_code.replace('XXXX','XL')
    roman_code = roman_code.replace('CCCC','CD')
    return roman_code
