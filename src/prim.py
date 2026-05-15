import heapq

def prim(grafo):
    """
    Algoritmo de Prim para encontrar el MST usando min-heap.
    Comienza desde S1 y crece agregando siempre la arista más barata.

    Args:
        grafo: dict con lista de adyacencia {nodo: [(vecino, peso)]}

    Retorna:
        mst: list de aristas del MST [(peso, nodo1, nodo2)]
        costo_total: int suma de pesos del MST
    """
    nodo_inicio = "S1"
    visitados = set()
    mst = []
    costo_total = 0

    # Cola de prioridad: (peso, nodo_origen, nodo_destino)
    heap = [(0, nodo_inicio, nodo_inicio)]

    while heap and len(visitados) < len(grafo):
        peso, origen, nodo = heapq.heappop(heap)

        if nodo in visitados:
            continue

        visitados.add(nodo)

        # No agregar la arista de inicio (peso 0, mismo nodo)
        if origen != nodo:
            mst.append((peso, origen, nodo))
            costo_total += peso

        # Explorar vecinos no visitados
        for vecino, costo in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(heap, (costo, nodo, vecino))

    return mst, costo_total