class UnionFind:
    """
    Estructura Union-Find con compresión de caminos y unión por rango.
    Se usa en Kruskal para detectar ciclos eficientemente.
    """

    def __init__(self, nodos):
        # Cada nodo es su propio representante al inicio
        self.padre = {nodo: nodo for nodo in nodos}
        # Rango para mantener el árbol balanceado
        self.rango = {nodo: 0 for nodo in nodos}

    def find(self, nodo):
        """
        Encuentra el representante del conjunto.
        Aplica compresión de caminos para futuras búsquedas.
        """
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.find(self.padre[nodo])
        return self.padre[nodo]

    def union(self, nodo1, nodo2):
        """
        Une los conjuntos de nodo1 y nodo2.
        Retorna False si ya estaban en el mismo conjunto (ciclo).
        """
        raiz1 = self.find(nodo1)
        raiz2 = self.find(nodo2)

        if raiz1 == raiz2:
            return False  # Formarían un ciclo

        # Unión por rango: el árbol más bajo queda debajo
        if self.rango[raiz1] < self.rango[raiz2]:
            self.padre[raiz1] = raiz2
        elif self.rango[raiz1] > self.rango[raiz2]:
            self.padre[raiz2] = raiz1
        else:
            self.padre[raiz2] = raiz1
            self.rango[raiz1] += 1

        return True
    