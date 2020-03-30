
def maiorValor(m):
    v = 0
    for x in range(len(m)):
        for y in range(len(m[0])):
            
            if m[x][y] > v:
                v = m[x][y]          
    return v
            
            

