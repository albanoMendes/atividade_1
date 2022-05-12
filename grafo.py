class Grafo:
	'''Classe que implementa a estrutura de dados Grafo.'''
	def __init__(self, direcionado=False, ponderado=False, num_vertices=0, num_arestas=0, vertices=[], arestas=[]):
		'''Inicializa os atributos e estruturas do grafo. Por default, são vazios.''' 
		self.direcionado = direcionado
		self.ponderado = ponderado
		self.num_vertices = num_vertices
		self.num_arestas = num_arestas
		self.aresta_default = float("inf") if ponderado else 0  # Valor default para arestas.

		# Inicializa as estruturas.
		if vertices:
			self.vertices = vertices  # Lista de rótulos de cada vértice.
		else:
			self.vertices = [None] * num_vertices  # Default.

		if arestas:
			self.arestas = arestas
		else:
			self.arestas = [[self.aresta_default]*num_vertices for i in range(num_vertices)] # Default.

	def qtdVertices(self):
		'''Número de vértices contidos no grafo.'''
		return self.num_vertices

	def qtdArestas(self):
		'''Número de arestas contidas no grafo.'''
		return self.num_arestas

	def grau(self, v):
		'''
		Grau de um vértice {v}, caso esteja no grafo.
		Em grafos direcionados retorna o grau entrante e sainte.
		'''
		if not self.haVertice(v): return None
		vizinhos = self.vizinhos(v)
		if self.direcionado:
			grau_entrante = len(vizinhos[0])
			grau_sainte = len(vizinhos[1])
			return (grau_entrante, grau_sainte)
		else:
			return len(vizinhos)

	def rotulo(self, v):
		'''Rótulo de um vértice {v}, caso esteja no grafo.'''
		return self.vertices[v-1] if self.haVertice(v) else None

	def vizinhos(self, v):
		'''
		Conjunto de vizinhos de um vértice {v}, caso esteja no grafo.
		Em grafos direcionados retorna os conjuntos de vizinhos entrantes e saintes.
		'''
		if not self.haVertice(v): return None
		if self.direcionado:
			entrantes = {i for i in range(1,self.num_vertices+1) if self.haAresta(i,v)}
			saintes = {i for i in range(1,self.num_vertices+1) if self.haAresta(v,i)}
			return (entrantes, saintes)
		else:
			return {i for i in range(1,self.num_vertices+1) if self.haAresta(v,i)}

	def haVertice(self, v):
		'''Checa se há um vértice {v} no grafo.'''
		return v in range(1,self.num_vertices+1)

	def getAresta(self, u, v):
		'''Retorna o valor de uma aresta/arco {u,v}. Em grafos ponderados, esse valor é o peso.'''
		return self.arestas[u-1][v-1] if self.haVertice(u) and self.haVertice(v) else self.aresta_default

	def haAresta(self, u, v):
		'''Checa se há uma aresta/arco {u,v} no grafo.'''
		return self.getAresta(u,v) != self.aresta_default

	def peso(self, u, v):
		'''Peso de uma aresta/arco {u,v}, caso o grafo seja ponderado.'''
		return self.getAresta(u,v) if self.ponderado else None

	def ler(self, filename):
		'''Lê um arquivo de grafo e inicializa os atributos e estruturas.'''
		with open(f"networks/{filename}", "r", encoding='utf-8') as graph_file:
			graph_data = graph_file.readlines()  # Lista contendo cada linha do arquivo de grafo.

		# Parsing das linhas do arquivo e inicialização das estruturas.
		self.num_vertices = int(graph_data[0].rstrip('\n').split()[1])
		self.num_arestas = len(graph_data) - self.num_vertices - 2
		self.vertices = [line.split('"')[-2] for line in graph_data[1:self.num_vertices+1]]
		self.arestas = [[self.aresta_default]*self.num_vertices for i in range(self.num_vertices)]

		# Atualiza a matriz de arestas apropriadamente para grafos ponderados ou não.
		for line in graph_data[self.num_vertices+2:]:
			line = line.split()
			u, v = map(int, line[:2])
			value = float(line[-1]) if self.ponderado else 1
			self.arestas[u-1][v-1] = value
			if not self.direcionado:
				self.arestas[v-1][u-1] = value 


if __name__ ==	"__main__":
	# Exemplo de inicialização e utilização de um objeto da classe Grafo.
	grafo = Grafo(direcionado=False, ponderado=False) 
	filename = "ContemCicloEuleriano.net"
	grafo.ler(filename)
	print(f"Arquivo de grafo lido: {filename}")

	u, v, w = 3, 5, 1  # Vértices para testes.
	print(f"Quantidade de vértices: {grafo.qtdVertices()}")
	print(f"Quantidade de arestas: {grafo.qtdArestas()}")
	print(f"Grau do vértice {{{u}}}: {grafo.grau(u)}")
	print(f"Rótulo do vértice {{{u}}}: {grafo.rotulo(u)}")
	print(f"Vizinhos do vértice {{{u}}}: {grafo.vizinhos(u)}")
	print(f"Há aresta entre os vértices {{{u}}} e {{{v}}}: {'Sim' if grafo.haAresta(u,v) else 'Não'}")
	print(f"Há aresta entre os vértices {{{u}}} e {{{w}}}: {'Sim' if grafo.haAresta(u,w) else 'Não'}")
	print(f"Peso da aresta {{{u},{v}}}: {grafo.peso(u,v)}")
	print(f"Peso da aresta {{{u},{w}}}: {grafo.peso(u,w)}")
