import sys
from grafo import Grafo
import random

def buscarSubcicloEuleriano(grafo, v,C):


grafo = Grafo(direcionado=False, ponderado=False)
grafo.ler(sys.argv[1])  # Lê o arquivo de grafo passado como argumento.
s = int(sys.argv[2])  # Define o vértice de origem passado como argumento.

C = []
for v in range(grafo.qtdVertices()):
   if (v + 1) < grafo.qtdVertices() and grafo.haAresta(v, v+1):
       C.append({v, v+1}, False)
n = random.randint(0,grafo.qtdVertices())
v = grafo.vertices[n];
(r, ciclo) = buscarSubcicloEuleriano(grafo, v,C)