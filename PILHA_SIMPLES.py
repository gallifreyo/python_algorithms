# pilha(stack)
#push - insercao
#pop - remocao
#s.length() -> comprimento da Pilha
import time

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if not self.empty():
            self.stack.pop(len(self.stack) - 1)
            
    def top(self):
        if not self.empty():
            return self.stack[-1]
        return "---------------\nPilha vazia !!!\n---------------"
        
    def empty(self):
        if (len(self.stack) == 0):
            return True
        return False
    
s = Stack()
# --------------------------------------------------


primeiro = 1
segundo = 2
terceiro = 3

print(" primeiro = 1")
print(" segundo = 2")
print(" terceiro = 3")

while True:
    print("---------------------")
    print("1 - Adicionar a Pilha")
    print("2 - Retirar da Pilha")
    print("3 - Ver ultimo elemento")
    print("4 - Verificar se esta vazia")
    r = int(input("Qual deseja usar ?: "))
    if(r == 1):
        num = int(input("Digite o numero que deseja adicionar(de 1 a 3): "))
        if(num == primeiro):
            s.push(1)
        elif(num == segundo):
            s.push(2)
        elif(num == terceiro):
            s.push(3)
        print(s.top())
        if(s.empty() == False):
            print("--------------------------")
            print("Adicionado com sucesso !")
            print("--------------------------")
        else:
            print("--------------------")
            print("Falha ao adicionar")
            print("--------------------")
    if(r == 2):
        s.pop()
    if(r == 3):
        print(s.top())
    if(r == 4):
        v = s.empty()
        if(v == False):
            print("----------------------")
            print("Pilha nao esta vazia")
            print("----------------------")
        else:
            print("-------------")
            print("Pilha vazia")
            print("-------------")
    time.sleep(3)
    
        














