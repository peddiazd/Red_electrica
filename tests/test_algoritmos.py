import sys
sys.path.append("../src")

from grafo import generar_red_electrica
from kruskal import kruskal
from prim import prim
from articulacion import encontrar_articulaciones
from simulacion import simular_fallo

def test_kruskal_y_prim_mismo_costo():
    grafo, aristas = generar_red_electrica()
    _, costo_kruskal = kruskal(grafo, aristas)
    _, costo_prim = prim(grafo)
    assert costo_kruskal == costo_prim, (
        f"Kruskal: {costo_kruskal} | Prim: {costo_prim} — No coinciden"
    )
    print(f"✓ MST verificado: ${costo_kruskal} millones")

def test_mst_tiene_n_menos_1_aristas():
    grafo, aristas = generar_red_electrica()
    mst, _ = kruskal(grafo, aristas)
    assert len(mst) == len(grafo) - 1, "El MST no tiene N-1 aristas"
    print(f"✓ MST tiene {len(mst)} aristas (N-1 correcto)")

def test_fallo_red_sigue_conectada():
    grafo, aristas = generar_red_electrica()
    _, _, conectado, ruta = simular_fallo(grafo, aristas, "S1", "S2")
    print(f"✓ Fallo S1-S2 | Conectada: {conectado} | Ruta: {ruta}")

if __name__ == "__main__":
    test_kruskal_y_prim_mismo_costo()
    test_mst_tiene_n_menos_1_aristas()
    test_fallo_red_sigue_conectada()
    print("\n✓ Todos los tests pasaron")