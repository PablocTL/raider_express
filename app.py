from db import obtener_platos
from pedidos import crear_pedido
from rutas import cargar_grafo, dijkstra, camino, rider_mas_cercano
from turno import planificar_turno
# pedir(), asignar() y ruta(): piden los datos con input() y llaman a las de arriba

def main():
    grafo = cargar_grafo()
    opciones = {
        "1": ("Ver la carta",           lambda: print(*obtener_platos(), sep="\n")),
        "2": ("Hacer un pedido",        lambda: pedir(grafo)),
        "3": ("Rider para un pedido",   lambda: asignar(grafo)),
        "4": ("Ruta entre dos barrios", lambda: ruta(grafo)),
        "5": ("Planificar el turno",    lambda: print(planificar_turno())),
    }
    while True:
        for k, (texto, _) in opciones.items():
            print(k, texto)
        eleccion = input("Opción (q para salir): ")
        if eleccion == "q":
            break
        opciones.get(eleccion, ("", lambda: print("No existe")))[1]()

if __name__ == "__main__":
    main()