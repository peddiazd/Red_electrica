from grafo import generar_red_electrica, mostrar_grafo
from kruskal import kruskal
from prim import prim
from articulacion import encontrar_articulaciones
from collections import deque

def simular_fallo(grafo, aristas, nodo1_fallo, nodo2_fallo):
    """
    Simula el fallo de una línea entre nodo1_fallo y nodo2_fallo.
    Recalcula el MST sin esa línea y busca ruta alternativa.

    Retorna:
        nuevo_mst: MST recalculado
        nuevo_costo: costo del nuevo MST
        conectado: bool si la red sigue conectada
        ruta: ruta alternativa entre los nodos afectados
    """
    # Eliminar la arista fallida de la lista
    par_fallo = tuple(sorted([nodo1_fallo, nodo2_fallo]))
    aristas_sin_fallo = [
        (p, n1, n2) for p, n1, n2 in aristas
        if tuple(sorted([n1, n2])) != par_fallo
    ]

    # Eliminar del grafo
    grafo_sin_fallo = {nodo: [] for nodo in grafo}
    for nodo, conexiones in grafo.items():
        for vecino, peso in conexiones:
            if tuple(sorted([nodo, vecino])) != par_fallo:
                grafo_sin_fallo[nodo].append((vecino, peso))

    # Recalcular MST
    nuevo_mst, nuevo_costo = kruskal(grafo_sin_fallo, aristas_sin_fallo)

    # Verificar conectividad con BFS
    ruta = bfs_ruta(grafo_sin_fallo, nodo1_fallo, nodo2_fallo)
    conectado = len(nuevo_mst) == len(grafo) - 1

    return nuevo_mst, nuevo_costo, conectado, ruta


def bfs_ruta(grafo, origen, destino):
    """
    Encuentra la ruta más corta (en saltos) entre origen y destino.
    Retorna la ruta como lista de nodos, o None si no existe.
    """
    cola = deque([[origen]])
    visitados = {origen}

    while cola:
        camino = cola.popleft()
        nodo_actual = camino[-1]

        if nodo_actual == destino:
            return camino

        for vecino, _ in grafo[nodo_actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(camino + [vecino])

    return None


if __name__ == "__main__":
    # Generar red
    grafo, aristas = generar_red_electrica()
    mostrar_grafo(grafo, aristas)

    # Calcular MST con ambos algoritmos
    mst_kruskal, costo_kruskal = kruskal(grafo, aristas)
    mst_prim, costo_prim = prim(grafo)

    print(f"\nCosto MST Kruskal : ${costo_kruskal} millones")
    print(f"Costo MST Prim    : ${costo_prim} millones")
    print(f"Verificación      : {'✓ Coinciden' if costo_kruskal == costo_prim else '✗ Difieren'}")

    # Detectar subestaciones críticas
    criticas = encontrar_articulaciones(grafo)
    print(f"\nSubestaciones críticas: {criticas}")

    # Simular fallo en la línea S1-S2
    print("\nSimulando fallo en línea S1-S2...")
    nuevo_mst, nuevo_costo, conectado, ruta = simular_fallo(grafo, aristas, "S1", "S2")
    print(f"Red sigue conectada : {conectado}")
    print(f"Nuevo costo MST     : ${nuevo_costo} millones")
    print(f"Ruta alternativa    : {' → '.join(ruta) if ruta else 'No existe'}")
    