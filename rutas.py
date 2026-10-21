
import heapq

def cargar_grafo():
    grafo = {
        "Carabanchel": {"Centro": 4, "Usera": 3},
        "Centro": {"Carabanchel": 4, "Retiro": 2, "Chamberi": 3},
        "Usera": {"Carabanchel": 3, "Retiro": 5},
        "Retiro": {"Centro": 2, "Usera": 5, "Chamberi": 4},
        "Chamberi": {"Centro": 3, "Retiro": 4}}
    return grafo

def dijkstra(grafo, origen):
    distancias = {nodo: float("inf") for nodo in grafo}
    anteriores = {nodo: None for nodo in grafo}
    distancias[origen] = 0
    cola = [(0, origen)]
    visitados = set()
    while cola:
        distancia, actual = heapq.heappop(cola)
        if actual in visitados:
            continue
        visitados.add(actual)
        for vecino, peso in grafo[actual].items():
            nueva_distancia = distancia + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual
                heapq.heappush(
                    cola, (nueva_distancia, vecino))
    return distancias, anteriores

def camino(anteriores, destino):
    ruta = []
    while destino is not None:
        ruta.append(destino)
        destino = anteriores[destino]
    ruta.reverse()
    return ruta

def rider_mas_cercano(grafo, origen, riders):
    distancias, anteriores = dijkstra(grafo, origen)
    rider_cercano = None
    distancia_minima = float("inf")
    for rider in riders:
        if rider in distancias and distancias[rider] < distancia_minima:
            distancia_minima = distancias[rider]
            rider_cercano = rider
    if rider_cercano is None:
        return None, float("inf"), []
    ruta = camino(anteriores, rider_cercano)
    return rider_cercano, distancia_minima, ruta