import networkx as nx
import matplotlib.pyplot as plt
from rutas import cargar_grafo, dijkstra, camino, rider_mas_cercano

grafo = cargar_grafo()

G = nx.Graph()
for origen in grafo:
    for destino, distancia in grafo[origen].items():
        G.add_edge(origen, destino, weight=distancia)
posiciones = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    posiciones,
    with_labels=True,
    node_color="lightblue",
    node_size=2500,
    font_size=9)

etiquetas = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(G, posiciones, edge_labels=etiquetas)
plt.title("Grafo de rutas")
plt.show()

distancias, anteriores = dijkstra(grafo, "Carabanchel")

print("Distancias desde Carabanchel:")
print(distancias)
print("Camino hasta Chamberi:")
print(camino(anteriores, "Chamberi"))

riders = ["Usera", "Retiro", "Chamberi"]
print("Repartidor más cercano:")
print(rider_mas_cercano(grafo, "Carabanchel", riders))

from rutas import dijkstra, camino
origen = "Carabanchel"
destino = "Chamberi"
distancias, anteriores = dijkstra(grafo, origen)
ruta = camino(anteriores, destino)
print("Origen:", origen)
print("Destino:", destino)
print("Distancia mínima:", distancias[destino])
print("Ruta más corta:", " -> ".join(ruta))