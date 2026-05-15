import matplotlib
matplotlib.use('Agg')  # Backend sin pantalla, debe ir antes de importar pyplot
import matplotlib.pyplot as plt
import networkx as nx
from grafo import generar_red_electrica
from kruskal import kruskal
from articulacion import encontrar_articulaciones

def visualizar_red(grafo, aristas, mst, criticas, arista_fallo=None, ruta=None, nombre_archivo="red_electrica.png"):
    """
    Visualiza la red eléctrica completa con el MST resaltado.
    Guarda la imagen como PNG en lugar de mostrarla en pantalla.

    Args:
        grafo: dict lista de adyacencia
        aristas: list todas las aristas
        mst: list aristas del MST
        criticas: set nodos de articulación
        arista_fallo: tuple (nodo1, nodo2) línea fallida opcional
        ruta: list ruta alternativa opcional
        nombre_archivo: str nombre del archivo PNG de salida
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

    # Colores de nodos: rojo si es crítico, azul si es normal
    colores_nodos = []
    for nodo in G.nodes():
        if nodo in criticas:
            colores_nodos.append("red")
        else:
            colores_nodos.append("steelblue")

    plt.figure(figsize=(14, 9))

    # Aristas no MST en gris punteado
    aristas_no_mst = [
        (n1, n2) for n1, n2 in G.edges()
        if (min(n1, n2), max(n1, n2)) not in aristas_mst
    ]
    nx.draw_networkx_edges(G, pos, edgelist=aristas_no_mst,
                           style="dashed", edge_color="lightgray", width=1)

    # MST en verde
    aristas_mst_lista = [
        (n1, n2) for n1, n2 in G.edges()
        if (min(n1, n2), max(n1, n2)) in aristas_mst
    ]
    nx.draw_networkx_edges(G, pos, edgelist=aristas_mst_lista,
                           edge_color="green", width=2.5)

    # Arista fallida en rojo punteado
    if arista_fallo and G.has_edge(*arista_fallo):
        nx.draw_networkx_edges(G, pos, edgelist=[arista_fallo],
                               edge_color="red", style="dashed", width=2.5)

    # Ruta alternativa en naranja
    if aristas_ruta:
        ruta_lista = [
            (n1, n2) for n1, n2 in G.edges()
            if (min(n1, n2), max(n1, n2)) in aristas_ruta
        ]
        nx.draw_networkx_edges(G, pos, edgelist=ruta_lista,
                               edge_color="orange", width=2.5)

    # Nodos y etiquetas
    nx.draw_networkx_nodes(G, pos, node_color=colores_nodos, node_size=700)
    nx.draw_networkx_labels(G, pos, font_color="white", font_size=8, font_weight="bold")

    # Pesos en las aristas
    pesos = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos, font_size=7)

    # Leyenda manual
    leyenda = [
        plt.Line2D([0], [0], color="green", linewidth=2.5, label="MST (red óptima)"),
        plt.Line2D([0], [0], color="lightgray", linewidth=1, linestyle="dashed", label="Conexiones no MST"),
        plt.Line2D([0], [0], color="red", linewidth=2.5, linestyle="dashed", label="Línea fallida"),
        plt.Line2D([0], [0], color="orange", linewidth=2.5, label="Ruta alternativa"),
        plt.scatter([0], [0], color="red", s=100, label="Subestación crítica"),
        plt.scatter([0], [0], color="steelblue", s=100, label="Subestación normal"),
    ]
    plt.legend(handles=leyenda, loc="upper left", fontsize=8)

    # Título con costos
    costo_mst = sum(p for p, _, _ in mst)
    costo_total = sum(p for p, _, _ in aristas)
    plt.title(
        f"Red Eléctrica Inteligente\n"
        f"Costo MST: ${costo_mst}M  |  Costo red completa: ${costo_total}M  |  "
        f"Ahorro: ${costo_total - costo_mst}M",
        fontsize=11
    )

    plt.axis("off")
    plt.tight_layout()

    # Guardar como PNG
    plt.savefig(nombre_archivo, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"✓ Visualización guardada como: {nombre_archivo}")


if __name__ == "__main__":
    from simulacion import simular_fallo

    grafo, aristas = generar_red_electrica()
    mst, _ = kruskal(grafo, aristas)
    criticas = encontrar_articulaciones(grafo)

    # Imagen 1: red normal con MST
    visualizar_red(grafo, aristas, mst, criticas,
                   nombre_archivo="../docs/red_normal.png")

    # Imagen 2: simulando fallo en S1-S2
    nuevo_mst, _, _, ruta = simular_fallo(grafo, aristas, "S1", "S2")
    visualizar_red(grafo, aristas, nuevo_mst, criticas,
                   arista_fallo=("S1", "S2"),
                   ruta=ruta,
                   nombre_archivo="../docs/red_fallo_S1_S2.png")