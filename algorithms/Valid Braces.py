def valid_braces(string):
    opposites = {'(':')','{':'}','[':']'}
    pairs = []
    for i in string:
        if i in ('(','{','['):
            pairs.append(i)
        else:
            if not pairs:
                return False
            elif i == opposites[pairs[-1]]:
                pairs.pop()
            else:
                return False
    return not pairs
