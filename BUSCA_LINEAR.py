
def busca(v, x):

    
    for k in range(len(vet)):

        if v[k] == x:
            return k
    return -1

vet = [0]*10
vet[2] = 1



print(busca(vet, 1))
