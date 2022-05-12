import sys
from grafo import Grafo

grafo = Grafo(direcionado=True, ponderado=True)
grafo.ler(sys.argv[1])  # Lê o arquivo de grafo passado como argumento.
s = int(sys.argv[2])  # Define o vértice de origem passado como argumento.

# Inicialização das estruturas.
distancias = [float("inf")] * grafo.qtdVertices()
antecessores = [None] * grafo.qtdVertices()
distancias[s-1] = 0  # Inicializa o vértice de origem.

for i in range(1, grafo.qtdVertices()):
	for u in range(1, grafo.qtdVertices()+1):
		for v in range(1, grafo.qtdVertices()+1):
			# Relaxamento.
			if grafo.haAresta(u,v):
				d = distancias[u-1] + grafo.peso(u,v)
				if distancias[v-1] > d:
					distancias[v-1] = d
					antecessores[v-1] = u

for u in range(1, grafo.qtdVertices()+1):
	for v in range(1, grafo.qtdVertices()+1):
		if grafo.haAresta(u,v):
			d = distancias[u-1] + grafo.peso(u,v)
			if distancias[v-1] > d:
				print("Há ciclo negativo.")
				exit()  # Termina o programa se um ciclo negativo foi detectado.

for u in range(1, grafo.qtdVertices()+1):
	caminho = []
	v = u
	while v:
		caminho.append(str(v))
		v = antecessores[v-1]
	print(f"{u}: {','.join(caminho[::-1])}; d={distancias[u-1]}")
