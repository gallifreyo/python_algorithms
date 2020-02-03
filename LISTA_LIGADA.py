class Node:

    def __init__(self, label):
        self.label = label
        self.next = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getNext(self):
        return self.next

    def setNext(self , next):
        self.next = next
        

class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):

        if index >= 0:
            #cria um novo nó
            node = Node(label)
            #verif se a lista esta vbazia
            if self.empty():
                self.first = node
                self.last = node
            else:
                if index == 0:
                    
                    #insercao no inicio
                    
                    node.setNext(self.first)
                    self.first = node
                    
                elif index >= self.len_list:
                    
                    #insercao no final
                    
                    self.last.setNext(node)
                    self.last = node
                    
                else:
                    #insercao no meio percorrer a lista
                    prev_node = self.first
                    curr_node = self.first.getNext()
                    curr_index = 1

                    while curr_node != None:
                        if curr_index == index:
                            #seta o curr_node como o proximo do no
                            node.setNext(curr_node)
                            #seta o node como o proximo do prev node
                            prev_node.setNext(node)
                            break
                        prev_node = curr_node
                        curr_node = curr_node.getNext()
                        curr_index += 1

                #atualiza o tamanho da lista
                self.len_list += 1

    def pop(self, index):

        if not self.empty() and index >= 0 and index < self.len_list:
            #se nao for vazio e index nao for negativo e index for menor do que a lista
            flag_remove = False
            #verif se foi removido ou nao

            if self.first.getNext() == None:
                # se possui apenas 1 elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                #remove do inicio mas possui mais de 1 elemento
                self.first = self.first.getNext()
                #self.first agora e o proximo do first
                flag_remove = True
            else:
                """
                        Se esta aqui e porque a lista possui mais de 1 elemento
                        e a remocao nao e no inicio.
                """
                prev_node = self.first
                curr_node = self.first.getNext()
                curr_index +=1
                    
                while curr_node != None:

                    if index == curr_index:
                        # o proximo do anterior aponta para o proximo do no corrente
                        prev_node.setNext(curr_node.getNext())
                        curr_node.setNext(None)
                        flag_remove = True
                        break
                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index +=1
                        
            if flag_remove:
                #se removeu atualiza o tamanho da lista
                self.len_list +=1
                    
    def empty(self):
        if self.first == None:
            return True
        return False

    def lenght(self):
        return self.len_list

    def show(self):

        curr_node = self.first

        while curr_node != None: 
            print(curr_node.getLabel(), end=' ')
            curr_node = curr_node.getNext()
        print("")

lista = LinkedList()

#teste insercao
lista.push('marcos',0)
lista.push('maria',1)
lista.push('jorge',2)
lista.push('amadeus',3)
lista.show()
print("Tamanho da lista = {}".format(lista.lenght()))








            
