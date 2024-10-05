def remove_duplicates(t):
    new = []
    for i in t:
        if i not in new:
            new.append(i)
    return new