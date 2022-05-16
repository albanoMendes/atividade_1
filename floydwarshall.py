import sys
from grafo import Grafo

grafo = Grafo(direcionado=True, ponderado=True)
grafo.ler(sys.argv[1])  # Lê o arquivo de grafo passado como argumento.
verts=grafo.qtdVertices() #"Verts" será usado como o número de vértices no grafo
distancias=[[float("inf") for x in range (0,verts)] for y in range(0,verts)]
#Inicialmente, valor infinito de distancia entre todos os pares




#CONSTRUÇÃO DE D(0)= Peso dos vértices diretamente ligados por arestas/ infinito para vérices não ligados
for u in range(1, verts+1):
	for v in range(1, verts+1):
		if grafo.haAresta(u,v):
			distancias[u-1][v-1] = grafo.peso(u,v)

for u in range (0,verts):
    distancias[u][u]=0
    #Distancia de um vertice para si mesmo é sempre 0

for i in range(0,verts): #I= Cada Vértice do grafo, para ser usado como conexão para achar caminho mínimo entre pares
    for u in range(0,verts): #U e V: pares a encontrar o caminho mínimo
        for v in range(0,verts):
            distancias[u][v]= min(distancias[u][v],(distancias[u][i]+distancias[i][v]))
#Distancia entre pares é o mínimo entre distancia de matriz anterior e distancia passando por I.


for u in range(0,verts):
	print(f"{u+1}: {','.join(map(str,distancias[u]))}")
