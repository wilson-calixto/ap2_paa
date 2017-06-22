
class Item(object):
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

    def get_peso(self):
        return self.peso
    
    def get_valor(self):
        return self.valor


def partition(list, start, end):
    pivot = list[end]
    bottom = start-1
    top = end

    done = 0
    while not done:

        while not done:
            bottom = bottom + 1

            if bottom == top:
                done = 1
                break

            if list[bottom].get_valor() > pivot.get_valor():
                list[top] = list[bottom]
                break

        while not done:
            top = top-1

            if top == bottom:
                done = 1
                break

            if list[top].get_valor() < pivot.get_valor():
                list[bottom] = list[top]
                break

    list[top] = pivot
    return top

def quicksort(list, start, end):
   if start < end:
        split = partition(list, start, end)
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
   else:
        return


def guloso(capacidade,valor_minimo_de_peso,itens):
    peso_livre_corrente=capacidade
    melhor_solução=0
    start = 0
    end = len(itens)-1
    quicksort(itens,start,end)
    itens=itens[::-1]
    solução=[]
    #completa vetor
    for i in range(len(itens)):
        solução.append(0)
    i=0
    while(i<len(itens)):

        if(itens[i].get_peso()<=peso_livre_corrente):
            peso_livre_corrente=peso_livre_corrente-itens[i].get_peso()
            solução[i]=1
            melhor_solução=melhor_solução+itens[i].get_valor()        
        i+=1
    if(melhor_solução>=valor_minimo_de_peso):
        return solução[::-1]
    else:
        return None
    
if __name__=="__main__":
    #completa vetor
    
    itens=[]
    item=Item(1,1)
    itens.append(item)
    item=Item(2,6)
    itens.append(item)
    item=Item(5,18)
    itens.append(item)
    item=Item(6,22)
    itens.append(item)
    item=Item(7,28)
    itens.append(item)
    
    capacidade=11
    valor_minimo_de_peso=0
    resposta=guloso(capacidade,valor_minimo_de_peso,itens)

  
    print("val:peso")
    for i in itens:
        print(i.get_valor()," : ", i.get_peso())
    print("resposta")
    print(resposta)        
