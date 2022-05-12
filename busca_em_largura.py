import sys
from collections import deque, defaultdict
from grafo import Grafo

grafo = Grafo(direcionado=True, ponderado=False)
grafo.ler(sys.argv[1])  # Lê o arquivo de grafo passado como argumento.
s = int(sys.argv[2])  # Define o vértice de origem passado como argumento.

# Inicialização das estruturas.
conhecidos = [False] * grafo.qtdVertices()
distancias = [float("inf")] * grafo.qtdVertices()
antecessores = [None] * grafo.qtdVertices()

# Inicizaliza o vértice de origem nas estruturas.
conhecidos[s-1] = True
distancias[s-1] = 0

# Prepara a fila de visitas, já incluindo o vértice de origem.
visitas = deque([s])

# Propagação das visitas.
while visitas:
	u = visitas.popleft()  # Desenfileira um vértice {u} da fila.
	# Percorre os vizinhos {v} do vértice {u}.
	entrantes, vizinhos_saintes = grafo.vizinhos(u)
	for v in vizinhos_saintes:
		# Atualiza as estruturas caso o vizinho {v} ainda não tenha sido visitado.
		if not conhecidos[v-1]:
			conhecidos[v-1] = True
			distancias[v-1] = distancias[u-1] + 1
			antecessores[v-1] = u
			visitas.append(v)  # Enfileira o vizinho {v}.

# Mostra os vértices de cada nível da busca em largura.
niveis = defaultdict(list)
for vertice, distancia in enumerate(distancias, start=1):
	if distancia < float("inf"):
		niveis[distancia].append(vertice)

for nivel, vertices in sorted(niveis.items()):
	print(f"{nivel}: {','.join(map(str,vertices))}")
