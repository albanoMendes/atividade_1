from operator import truediv
import sys
from grafo import Grafo
import random

def buscarSubcicloEuleriano(grafo, v,C):
    ciclo=[v]
    t=v
    vizinhosv=grafo.vizinhos(v)
    vdiferenteT=True
    while v!=t:
        for vizinho in vizinhosv:
            for ligacao in C:
                if ligacao==({v,vizinho},False):
                    ligacao=({v,vizinho},False)
                    v=ligacao
                    ciclo.append(v)
                    if v==t:
                        vdiferenteT=False

    
    
    return (False,[0])
        


grafo = Grafo(direcionado=False, ponderado=False)
grafo.ler(sys.argv[1])  # Lê o arquivo de grafo passado como argumento.
#s = int(sys.argv[2])  # Define o vértice de origem passado como argumento.

#   LINHAS 1 A 2 DO CICLO
C = []
for v in range(0,grafo.qtdVertices()):
    for v2 in range(0,grafo.qtdVertices()):
      if grafo.haAresta(v, v2):
       C.append({v, v2}, False)


n = random.randint(0,grafo.qtdVertices())
v = grafo.vertices[n];
(r, ciclo) = buscarSubcicloEuleriano(grafo, v,C)


e=False

if r==False:
    print(0)


else:
    e=True
    for aresta in C:
        if aresta[1]==False:
            e=False
            print(0)
            
if e==True:
    print(1)
    print(ciclo)
