import random

vetor = [0]*10
vetor2 = [0]*10

tam = len(vetor)
x = 0

while x < tam:
    vetor[x] = int(random.randint(1,10))
    vetor2[x] = int(random.randint(1,10))
    x += 1






def inverte(vet, vet2):
    n = len(vet)
    soma = 0
    for i in range(n):
        vet2[n - i - 1] = vet[i]

print(vetor)
inverte(vetor, vetor2)
print(vetor2)

