import numpy as np
'''
def resolve_mochila(pesos,valores,capacidade):
    n=len(pesos)
    matriz_de_valores=[]
    
    for j in range(n+1):
      l=[]  
      for i in range(capacidade+1):
          l.append(0)
          
      matriz_de_valores.append(l)
      
    #matriz_de_marcacao=np.zeros([n+1,capacidade+1])
    
    for i in range(0,n+1): 
        for w in range(0,capacidade+1):
            if(pesos[i-1]>w):
                matriz_de_valores[i][w]=matriz_de_valores[i-1][w]
            else:
                matriz_de_valores[i][w]=max(matriz_de_valores[i-1][w],valores[i-1] + matriz_de_valores[i-1][(w-pesos[i-1])])
     #           if(matriz_de_valores[i-1][w]<matriz_de_valores[i-1][w-pesos[i-1]]+valores[i-1]):
                    #matriz_de_marcacao[i][w]=1#
                     
            
                
    return matriz_de_valores#,matriz_de_marcacao           

'''

def resolve_mochila(pesos,valores,capacidade):
    n=len(pesos)
    matriz_de_valores=np.zeros([n+1,capacidade+1])

    for i in range(1,n+1): # The item 0 considers the empty knapsack
        for w in range(0,capacidade+1):
            if(w-pesos[i-1]>=0):

                matriz_de_valores[i,w]=max(matriz_de_valores[i-1,w],matriz_de_valores[i-1,w-pesos[i-1]]+valores[i-1])
                
            else:
                matriz_de_valores[i,w]=matriz_de_valores[i-1,w]
    return matriz_de_valores 




def de_matriz_pra_indice(matriz_de_valores,pesos):
    [n,capacidade]=np.shape(matriz_de_valores)
    
    n=n-1
    capacidade=capacidade-1
    '''
    #vetor_resposta=[]
    #k=capacidade
    
    
    for i in range(n,0,-1):
        if(matriz_de_marcacao[i,k]==1):
            vetor_resposta.append(i-1)
            k=capacidade-pesos[i-1]                    
            '''
    maior=matriz_de_valores[-1][-1]
    novo_vet=[]
    i=n
    w=capacidade
    #for t in matriz_de_valores:
     #   print(t)
   # print("peso ",w)
    while (i>0 and w>0):
        if(matriz_de_valores[i][w]!=matriz_de_valores[i-1][w]):
          #  print("1: ",matriz_de_valores[i][w])
           # print("2: ",matriz_de_valores[i-1][w],"indice",i)
            novo_vet.append(i-1)
            #print("pesos na posicao i ",pesos[i-1])
            w=w-pesos[i-1]
            i=i-1
        else:
            i=i-1
            
    return novo_vet



lista_de_pesos=[]

lista_de_codigos=[]

lista_de_valores=[]


tam=int(input())
for i in range(tam):
    l=str(input())
    lista=[]
    lista=l.split(' ')
    if(lista[0]=="TOSD12"):
      pass
    else:
        
      lista_de_codigos.append(lista[0])
      
      numero=int(lista[1])
      lista_de_pesos.append(numero)
      numero1=float(lista[2])
  #    numero1=int(numero1)
      lista_de_valores.append(numero1)
      #novo_peso=rendimento/peso*100
    
capacidade=100000

   
matriz_de_valores= resolve_mochila(lista_de_pesos,lista_de_valores,capacidade)  
 
#vetor_ com os indices dos codigos
v=de_matriz_pra_indice(matriz_de_valores,lista_de_pesos)


# 1 2 3
resp=[]    
for i in v:
    if(i!=-1):
       resp.append(lista_de_codigos[i]) 

resp.sort()

for i in resp:
    print(i)

