def solution(roman : str) -> int:    
    nums = []
    roman_code = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    four_nine = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    
    for keys,values in four_nine.items():
        if keys in roman:
            nums.append(values*(roman.count(keys)))
            roman = roman.replace(keys,'')
    for i in roman:
        nums.append(roman_code[i])
    return sum(nums)
