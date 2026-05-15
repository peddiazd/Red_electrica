import matplotlib.pyplot as plt
import networkx as nx
from grafo import generar_red_electrica
from kruskal import kruskal
from articulacion import encontrar_articulaciones

def visualizar_red(grafo, aristas, mst, criticas, arista_fallo=None, ruta=None):
    """
    Visualiza la red eléctrica completa con el MST resaltado.

    Args:
        grafo: dict lista de adyacencia
        aristas: list todas las aristas
        mst: list aristas del MST
        criticas: set nodos de articulación
        arista_fallo: tuple (nodo1, nodo2) línea fallida opcional
        ruta: list ruta alternativa opcional
    """
    G = nx.Graph()

    # Agregar nodos y aristas al grafo de NetworkX
    for peso, nodo1, nodo2 in aristas:
        G.add_edge(nodo1, nodo2, weight=peso)

    pos = nx.spring_layout(G, seed=42)

    # Clasificar aristas por tipo
    aristas_mst = {(min(n1, n2), max(n1, n2)) for _, n1, n2 in mst}
    aristas_fallo_par = tuple(sorted(arista_fallo)) if arista_fallo else None
    aristas_ruta = set()
    if ruta:
        for i in range(len(ruta) - 1):
            aristas_ruta.add((min(ruta[i], ruta[i+1]), max(ruta[i], ruta[i+1])))

    # Colores de nodos
    colores_nodos = []
    for nodo in G.nodes():
        if nodo in criticas:
            colores_nodos.append("red")
        else:
            colores_nodos.append("steelblue")

    # Dibujar grafo base (aristas no MST en gris punteado)
    aristas_no_mst = [
        (n1, n2) for n1, n2 in G.edges()
        if (min(n1, n2), max(n1, n2)) not in aristas_mst
    ]
    nx.draw_networkx_edges(G, pos, edgelist=aristas_no_mst,
                           style="dashed", edge_color="lightgray", width=1)

    # Dibujar MST en verde
    aristas_mst_lista = [
        (n1, n2) for n1, n2 in G.edges()
        if (min(n1, n2), max(n1, n2)) in aristas_mst
    ]
    nx.draw_networkx_edges(G, pos, edgelist=aristas_mst_lista,
                           edge_color="green", width=2.5)

    # Dibujar arista fallida en rojo
    if arista_fallo:
        nx.draw_networkx_edges(G, pos, edgelist=[arista_fallo],
                               edge_color="red", style="dashed", width=2)

    # Dibujar ruta alternativa en naranja
    if aristas_ruta:
        ruta_lista = [
            (n1, n2) for n1, n2 in G.edges()
            if (min(n1, n2), max(n1, n2)) in aristas_ruta
        ]
        nx.draw_networkx_edges(G, pos, edgelist=ruta_lista,
                               edge_color="orange", width=2)

    # Dibujar nodos y etiquetas
    nx.draw_networkx_nodes(G, pos, node_color=colores_nodos,
                           node_size=600)
    nx.draw_networkx_labels(G, pos, font_color="white", font_size=8)

    # Etiquetas de pesos
    pesos = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos, font_size=7)

    # Leyenda
    costo_mst = sum(p for p, _, _ in mst)
    costo_total = sum(p for p, _, _ in aristas)
    plt.title(
        f"Red Eléctrica Inteligente\n"
        f"Costo MST: ${costo_mst}M  |  Costo red completa: ${costo_total}M",
        fontsize=11
    )
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    grafo, aristas = generar_red_electrica()
    mst, _ = kruskal(grafo, aristas)
    criticas = encontrar_articulaciones(grafo)
    visualizar_red(grafo, aristas, mst, criticas)