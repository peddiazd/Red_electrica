def encontrar_articulaciones(grafo):
    """
    Detecta nodos de articulación usando DFS.
    Un nodo de articulación es aquel cuya eliminación desconecta el grafo.

    Args:
        grafo: dict con lista de adyacencia

    Retorna:
        articulaciones: set con los nodos críticos
    """
    visitado = {}
    disc = {}      # Tiempo de descubrimiento
    low = {}       # Menor tiempo alcanzable
    padre = {}
    articulaciones = set()
    tiempo = [0]   # Lista para mutabilidad dentro de la función interna

    def dfs(nodo):
        visitado[nodo] = True
        disc[nodo] = low[nodo] = tiempo[0]
        tiempo[0] += 1
        hijos = 0

        for vecino, _ in grafo[nodo]:
            if vecino not in visitado:
                hijos += 1
                padre[vecino] = nodo
                dfs(vecino)

                # Actualizar low del nodo actual
                low[nodo] = min(low[nodo], low[vecino])

                # Caso 1: nodo raíz con más de un hijo
                if padre.get(nodo) is None and hijos > 1:
                    articulaciones.add(nodo)

                # Caso 2: nodo no raíz cuyo hijo no llega más arriba
                if padre.get(nodo) is not None and low[vecino] >= disc[nodo]:
                    articulaciones.add(nodo)

            elif vecino != padre.get(nodo):
                low[nodo] = min(low[nodo], disc[vecino])

    for nodo in grafo:
        if nodo not in visitado:
            padre[nodo] = None
            dfs(nodo)

    return articulaciones