import numpy as np

def resolve_mochila(pesos,valores,capacidade):
    n=len(pesos)
    matriz_de_valores=np.zeros([n+1,capacidade+1])
    matriz_de_marcacao=np.zeros([n+1,capacidade+1])
    for i in range(1,n+1): # The item 0 considers the empty knapsack
        for x in range(0,capacidade+1):
            if(x-pesos[i-1]>=0):

                matriz_de_valores[i,x]=max(matriz_de_valores[i-1,x],matriz_de_valores[i-1,x-pesos[i-1]]+valores[i-1])
                if(matriz_de_valores[i-1,x]<matriz_de_valores[i-1,x-pesos[i-1]]+valores[i-1]):
                    matriz_de_marcacao[i,x]=1
            else:
                matriz_de_valores[i,x]=matriz_de_valores[i-1,x]
    return matriz_de_valores,matriz_de_marcacao           

def de_matriz_pra_indice(matriz_de_marcacao,pesos):
    [n,capacidade]=np.shape(matriz_de_marcacao)
    n=n-1
    capacidade=capacidade-1
    vetor_resposta=[]
    k=capacidade
    for i in range(n,0,-1):
        if(matriz_de_marcacao[i,k]==1):
            vetor_resposta.append(i-1)
            k=capacidade-pesos[i-1]                    
    return vetor_resposta



lista_de_pesos=[]

lista_de_codigos=[]

lista_de_valores=[]


tam=int(input())
for i in range(tam):
    l=str(input())
    lista=[]
    lista=l.split(' ')
    lista_de_codigos.append(lista[0])
    numero=int(lista[1])
    lista_de_pesos.append(numero)
    numero1=float(lista[2])
    numero1=int(numero1)
    lista_de_valores.append(numero1)
    #novo_peso=rendimento/peso*100
    
capacidade=100000

    
    
[matriz_de_valores,matriz_de_marcacao]= resolve_mochila(lista_de_pesos,lista_de_valores,capacidade)  
v=de_matriz_pra_indice(matriz_de_marcacao,lista_de_pesos)

cap=matriz_de_valores[-1][-1]

for i in range(len(v)):
    if(cap-lista_de_valores[v[i]]>=0):
        cap=cap-lista_de_valores[v[i]]
    else:
        v[i]=-1

             

resp=[]    
for i in v:
    if(i!=-1):
       resp.append(lista_de_codigos[i]) 

resp.sort()

for i in resp:
    print(i)
