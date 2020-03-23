
matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

qtde = len(matriz[0])
for i in range(qtde):
    matriz[i][i] = 1
for z in range(qtde):
    print(matriz[z])
