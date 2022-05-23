from operator import truediv
import sys
from grafo import Grafo
import random

def existeVizinhoNaoVisitado(grafo, v,C):
    vizinhosv=grafo.vizinhos(v)
    for vizinho in vizinhosv:
        for ligacao in C:
            if ligacao==({v,vizinho},False):
                return True
    return False


def buscarSubcicloEuleriano(grafo, v,C):
    ciclo=[v]
    t=v
    vdiferenteT=True
    while vdiferenteT==True:
        if existeVizinhoNaoVisitado(grafo,v,C)==False:
            return False
        else:
            pass #continuar da linha 7 do subciclo
    
        


grafo = Grafo(direcionado=False, ponderado=False)
grafo.ler(sys.argv[1])  # Lê o arquivo de grafo passado como argumento.
#s = int(sys.argv[2])  # Define o vértice de origem passado como argumento.

#   LINHAS 1 A 2 DO ALGORITMO
C = []
for v in range(0,grafo.qtdVertices()):
    for v2 in range(0,grafo.qtdVertices()):
      if grafo.haAresta(v, v2):
       C.append({v, v2}, False)

#v<-Vértice aleatório de V
n = random.randint(0,grafo.qtdVertices())
v = grafo.vertices[n]
(r, ciclo) = buscarSubcicloEuleriano(grafo, v,C)


existeCiclo=0
#Se método chamado retornar falso, imprimir 0, não tem ciclo euleriano
if r==True: #caso contrario
    for aresta in C:
        if aresta[1]==False:
            existeCiclo=1           
            break
print(existeCiclo)
if existeCiclo==1:
    print(ciclo)
