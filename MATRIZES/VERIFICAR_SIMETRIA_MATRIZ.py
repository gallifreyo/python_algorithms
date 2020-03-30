  
def simetrica(m):
    t = len(m)
    d = 0
    for x in range(t):
        for y in range(t):
            d +=1
    if len(m[0]) == (d//len(m[0])):
        return True
    else:
        return False

