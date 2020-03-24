# supondo que as matrizes tem a mesma ordem


matriz_A = [[1,2,3],
            [4,5,6],
            [7,8,9]]
matriz_B = [[1,2,3],
            [4,5,6],
            [7,8,9]]

matriz_resp = [[0,0,0],
               [0,0,0],
               [0,0,0]]

tam = len(matriz_A[0])

for x in range(tam):
    for y in range(tam):
        matriz_resp[x][y] = matriz_A[x][y] + matriz_B[x][y]



for i in range(tam):
    print(matriz_resp[i])
    
    
        
    
