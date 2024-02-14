import heapq as hp

INFINITO = 10000000 # definindo um valor para infinito

class Grafo:
    vertices = int # número de vértices
    adjacencias = list # listá que irá conter o número de adjacencias
    def __init__(self, vertice:int):
        self.vertices = vertice
        self.adjacencias = [[] for _ in range(vertice)]

    def addAresta(self,verticeInicial:int,verticeFinal:int,custo:int) -> None:
        self.adjacencias[verticeInicial].append((verticeFinal,custo))
    
    def Dijkstra(self,origem:int,destino:int) -> list:
        distancias = [INFINITO] * self.vertices # vetor para guardar as distâncias
        verticesVisitados = [False] * self.vertices # vetor para verificar caso uma adjacência já tenha sido visitada, não ser visitada mais
        filaPrioridade = [] # fila de prioridades(menores custos para cada vertice)
        # definindo a distância para a origem 
        distancias[origem] = 0

        #iniciando a fila de prioridades com a origem
        hp.heappush(filaPrioridade,(distancias[origem],origem))

        while filaPrioridade:
            verticeOrigem = hp.heappop(filaPrioridade)[1] # pegando o vertice da origem

            if not verticesVisitados[verticeOrigem]:
                verticesVisitados[verticeOrigem] = True

                for i in range(len(self.adjacencias[verticeOrigem])):
                     vertice, distanciaAresta = self.adjacencias[verticeOrigem][i]
                     if distancias[vertice] > distancias[verticeOrigem] + distanciaAresta:
                        distancias[vertice] = distancias[verticeOrigem] + distanciaAresta
                        # colocando os menores valores de custo
                        hp.heappush(filaPrioridade,(distancias[vertice],vertice))
        
        return distancias[destino]
    
    def __str__(self) -> str:
        grafo_str = ""
        for i in range(self.vertices):
            for v, c in self.adjacencias[i]:
                grafo_str += f"({i}, {v}, {c})\n"
        return grafo_str

if __name__ == "__main__":
    g = Grafo(5)
    g.addAresta(0, 3, 11)
    g.addAresta(0, 2, 1)
    g.addAresta(0, 1, 6)
    g.addAresta(1, 4, 10)
    g.addAresta(2, 1, 5)
    g.addAresta(2, 3, 2)
    g.addAresta(2, 2, 15)
    g.addAresta(3, 4, 23)
    g.addAresta(4, 1, 32)
    g.addAresta(4, 0, 8)

    print(f'Menor custo de {1} a {3} é: {g.Dijkstra(1, 3)}')
    #print('Mostrando grafo')
    #print(g)


