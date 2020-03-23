
vet = [5,4,3,2,1]
vet2 = [0,0,0,0,0]

def inverte(x,y):
    tam = len(x)
    for i in range(tam):
        y[tam - i - 1] = x[i]

print(vet)
inverte(vet,vet2)
print(vet2)
