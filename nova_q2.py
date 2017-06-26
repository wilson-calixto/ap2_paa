import numpy as np

def solve_Knapsack_DP(weights,values,capacity):
    n=len(weights)
    valueFunction=np.zeros([n+1,capacity+1])
    contentMatrix=np.zeros([n+1,capacity+1])
    for i in range(1,n+1): # The item 0 considers the empty knapsack
        for x in range(0,capacity+1):
            if(x-weights[i-1]>=0):

                valueFunction[i,x]=max(valueFunction[i-1,x],valueFunction[i-1,x-weights[i-1]]+values[i-1])
                if(valueFunction[i-1,x]<valueFunction[i-1,x-weights[i-1]]+values[i-1]):
                    contentMatrix[i,x]=1
            else:
                valueFunction[i,x]=valueFunction[i-1,x]
    return valueFunction,contentMatrix           

def disclosure_content(contentMatrix,weights):
    [n,capacity]=np.shape(contentMatrix)
    n=n-1
    capacity=capacity-1
    content=[]
    k=capacity
    for i in range(n,0,-1):
        if(contentMatrix[i,k]==1):
            content.append(i-1)
            k=capacity-weights[i-1]                    
    return content



weightList=[]

codeList=[]

valueList=[]


tam=int(input())
for i in range(tam):
    l=str(input())
    lista=[]
    lista=l.split(' ')
    codeList.append(lista[0])
    peso=float(lista[1])
    weightList.append(int(peso))
    va=float(lista[2])
    valueList.append(round(int(va)))
    #novo_peso=rendimento/peso*100
    
capacity=100000

    
    
[valueFunction,contentMatrix]= solve_Knapsack_DP(weightList,valueList,capacity)  
print (valueFunction)
v=disclosure_content(contentMatrix,weightList)
print(v)
cap=valueFunction[-1][-1]#deixar gererico
print("gdsuygfsd ",cap)
for i in range(len(v)):
    if(cap-valueList[v[i]]>=0):
        cap=cap-valueList[v[i]]
    else:
        v[i]=-1


             
print(v)
    
for i in v:
   if(i!=-1):
     print(codeList[i])
