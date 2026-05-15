from union_find import UnionFind

def kruskal(grafo, aristas):
    """
    Algoritmo de Kruskal para encontrar el MST.
    Ordena las aristas por peso y las agrega si no forman ciclo.

    Args:
        grafo: dict con lista de adyacencia
        aristas: list de tuplas (peso, nodo1, nodo2)

    Retorna:
        mst: list de aristas del MST [(peso, nodo1, nodo2)]
        costo_total: int suma de pesos del MST
    """
    # Ordenar aristas de menor a mayor costo
    aristas_ordenadas = sorted(aristas)

    # Inicializar Union-Find con todos los nodos
    uf = UnionFind(grafo.keys())

    mst = []
    costo_total = 0

    for peso, nodo1, nodo2 in aristas_ordenadas:
        # Agregar arista solo si no forma un ciclo
        if uf.union(nodo1, nodo2):
            mst.append((peso, nodo1, nodo2))
            costo_total += peso

        # El MST de N nodos tiene exactamente N-1 aristas
        if len(mst) == len(grafo) - 1:
            break

    return mst, costo_total