
from operator import truediv
from re import sub
import sys
from grafo import Grafo
import random





grafo = Grafo(direcionado=False, ponderado=False)
grafo.ler(sys.argv[1])  # Lê o arquivo de grafo passado como argumento.
#s = int(sys.argv[2])  # Define o vértice de origem passado como argumento.


for u in range(1, grafo.qtdVertices()+1):
    if grafo.grau(u)%2!=0:
        print (0)
        exit()
#Verifica se todos os vértices tem grau par, caso contrário, já sabe-se que não é euleriano


C=[] #Lista das arestas
for v in range(1,grafo.qtdVertices()+1):
    for v2 in range(1,grafo.qtdVertices()+1):
      if grafo.haAresta(v, v2): #Adciona se houver arestas
          if [[v2,v],False] not in C:  #Mas cuida para não adcionar a mesma arestas 2 vezes
            C.append([[v,v2], False]) #Par de vértices e Bool para determinar se já foi visitada

n = random.randint(1,grafo.qtdVertices())
while grafo.vizinhos(n)==0:
    n = random.randint(1,grafo.qtdVertices())
#Escolhe vértice aleatório inicial


ciclo=[]
subciclo=[n]

while len(subciclo)!=0: #Enquanto o subciclo euleriano estiver não vazio
    if_taken=False 
    #Essa variável controla se, em alguma das várias repetições do for, entrou-se no if ao menos uma vez
    for aresta in C:
        
        if aresta[0][0]==subciclo[0] and aresta[1]==False: 
            if_taken=True

            #Substitui a aresta no vértice consigo mesma, mas com bool True
            index=C.index(aresta)
            C.insert(index,[[aresta[0][0],aresta[0][1]],True])
            C.remove(aresta)


            #Adciona valor vizinho como cabeça do subciclo
            subciclo.insert(0,aresta[0][1])
            break
        elif aresta[0][1]==subciclo[0] and aresta[1]==False:
            #Mesma coisa do if anterior, mas com a aresta salva com a ordem dos vértices ao contrário
            if_taken=True
            index=C.index(aresta)
            C.insert(index,[[aresta[0][0],aresta[0][1]],True])
            C.remove(aresta)
            subciclo.insert(0,aresta[0][0])
            break
    if not if_taken: #Se não entrou no if, então não há vizinhos não visitados
        #Remove cabeça do subciclo e coloca permanentemente no ciclo.
        ciclo.insert(0,subciclo[0])
        subciclo.remove(subciclo[0])
print (1)
print(f"{','.join(map(str,ciclo))}")

