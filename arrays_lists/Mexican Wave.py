def wave(people):
    # Code here
    if not people:
        return []
    w = []
    for i in range(len(people)):
        if people[i] == ' ':
            continue
        else:
            string = people[:i]+people[i].upper()+people[i+1:]
            w.append(string)
    return w
