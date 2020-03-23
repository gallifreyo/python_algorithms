import random

def mediaVet(y):
    soma = 0
    for s in range(0, tam):
        soma = soma + y[s]

        print("soma= ",soma)
        print("tam= ",tam)
        
    return (soma/tam)


vetor = [0]*10

tam = len(vetor)
x = 0

while x < tam:
    vetor[x] = int(random.randint(1,11))
    x += 1


    

print(vetor)

print(mediaVet(vetor))
