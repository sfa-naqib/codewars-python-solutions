def solution(s):
    if len(s) % 2:
        s = s + "_"
    pairs = []
    for i in range(0,len(s),2):
        pairs.append(s[i:i+2])
    return pairs
