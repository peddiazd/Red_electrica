import random

def generar_red_electrica(seed=42):
    """
    Genera una red eléctrica con 15 subestaciones (S1-S15)
    y 25 líneas de transmisión con costos aleatorios entre
    10 y 100 millones de pesos.
    Garantiza que cada nodo tenga mínimo 2 conexiones para
    que ninguna subestación quede sin respaldo ante un fallo.

    Retorna:
        grafo: dict con lista de adyacencia {nodo: [(vecino, peso)]}
        aristas: list con todas las aristas [(peso, nodo1, nodo2)]
    """
    random.seed(seed)

    nodos = [f"S{i}" for i in range(1, 16)]
    grafo = {nodo: [] for nodo in nodos}
    aristas_existentes = set()
    aristas = []

    # Paso 1: árbol generador para garantizar conectividad
    nodos_conectados = [nodos[0]]
    nodos_restantes = nodos[1:]

    for nodo in nodos_restantes:
        vecino = random.choice(nodos_conectados)
        peso = random.randint(10, 100)
        grafo[nodo].append((vecino, peso))
        grafo[vecino].append((nodo, peso))
        par = tuple(sorted([nodo, vecino]))
        aristas_existentes.add(par)
        aristas.append((peso, nodo, vecino))
        nodos_conectados.append(nodo)

    # Paso 2: garantizar mínimo 2 conexiones por nodo
    for nodo in nodos:
        if len(grafo[nodo]) < 2:
            # Buscar un nodo diferente con quien conectarse
            candidatos = [n for n in nodos
                         if n != nodo
                         and tuple(sorted([nodo, n])) not in aristas_existentes]
            if candidatos:
                vecino = random.choice(candidatos)
                peso = random.randint(10, 100)
                grafo[nodo].append((vecino, peso))
                grafo[vecino].append((nodo, peso))
                par = tuple(sorted([nodo, vecino]))
                aristas_existentes.add(par)
                aristas.append((peso, nodo, vecino))

    # Paso 3: agregar aristas hasta completar 25
    intentos = 0
    while len(aristas) < 25 and intentos < 1000:
        nodo1 = random.choice(nodos)
        nodo2 = random.choice(nodos)
        par = tuple(sorted([nodo1, nodo2]))
        if nodo1 != nodo2 and par not in aristas_existentes:
            peso = random.randint(10, 100)
            grafo[nodo1].append((nodo2, peso))
            grafo[nodo2].append((nodo1, peso))
            aristas_existentes.add(par)
            aristas.append((peso, nodo1, nodo2))
        intentos += 1

    return grafo, aristas


def mostrar_grafo(grafo, aristas):
    """
    Imprime el grafo y un resumen de la red generada.
    """
    print("=" * 45)
    print("   RED ELÉCTRICA — Lista de adyacencia")
    print("=" * 45)
    for nodo, conexiones in grafo.items():
        conexiones_str = ", ".join(
            f"{vecino}(${peso}M)" for vecino, peso in conexiones
        )
        print(f"  {nodo}: {conexiones_str}")

    print(f"\nTotal de subestaciones : {len(grafo)}")
    print(f"Total de líneas        : {len(aristas)}")
    costo_total = sum(p for p, _, _ in aristas)
    print(f"Costo total de la red  : ${costo_total} millones")
    print("=" * 45)
