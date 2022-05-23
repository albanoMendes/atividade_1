from operator import truediv
import sys
from grafo import Grafo
import random

def existeVizinhoNaoVisitado(grafo, v,C):
    vizinhosv=grafo.vizinhos(grafo.valor(v))
    try:
        for vizinho in vizinhosv:
            for ligacao in C:
                if ligacao==([[v,grafo.rotulo(vizinho-1)],False]):
                    return True
    except:
        return False
    return False


def buscarSubcicloEuleriano(grafo, v,C):
    ciclo=[v]
    t=v
    vdiferenteT=True
    while vdiferenteT==True:
        if existeVizinhoNaoVisitado(grafo,v,C)==False:
            return [False,[0]]
        else:
            print('a')
            for aresta in C:
                if aresta[0][0]==v and aresta[1]==False:
                    aresta[1]==True
                    v=aresta[0][1]
                    ciclo.append(v)
                    if v==t:
                        vdiferenteT==False
                    break
    for x in ciclo:
        if existeVizinhoNaoVisitado(grafo,x,C):
            r,ciclo2=buscarSubcicloEuleriano(grafo,x,C)
            if r==False:
                return [False,[0]]
            for i in range(0,len(ciclo)):
                if ciclo[i]==ciclo2[0]:
                    ciclo= ciclo[0:i] + ciclo2[0:]
                    break
            return[True,ciclo]
    
        


grafo = Grafo(direcionado=False, ponderado=False)
grafo.ler(sys.argv[1])  # Lê o arquivo de grafo passado como argumento.
#s = int(sys.argv[2])  # Define o vértice de origem passado como argumento.

#   LINHAS 1 A 2 DO ALGORITMO
C = []
for v in range(1,grafo.qtdVertices()+1):
    for v2 in range(1,grafo.qtdVertices()+1):
      if grafo.haAresta(v, v2):
       C.append([[grafo.rotulo(v),grafo.rotulo(v2)], False])

#v<-Vértice aleatório de V
n = random.randint(0,grafo.qtdVertices())

v = grafo.vertices[n-1]
retornosub = buscarSubcicloEuleriano(grafo, v,C)

r=retornosub[0]
ciclo=retornosub[1]

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
