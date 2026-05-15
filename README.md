# Simulador de Red Eléctrica Inteligente

**Universidad Cooperativa de Colombia — Estructura de Datos 2026**
**Docente:** Diego León Arcila Herrera
**Estudiante:** Pedro Díaz
**Código:** 96000
**Programa:** Ingeniería de Software

---

## Descripción

Simulador de una red eléctrica inteligente donde 15 subestaciones están
conectadas por líneas de transmisión con diferentes costos de instalación
en millones de pesos. El sistema encuentra la red más económica posible
usando algoritmos de Árbol de Expansión Mínima y garantiza que ante
cualquier fallo en una línea o subestación la energía se redirija
automáticamente por rutas alternativas.

## Resultados obtenidos

| Métrica | Valor |
|---|---|
| Subestaciones | 15 |
| Líneas de transmisión | 25 |
| Costo red completa | $1.224 millones |
| Costo MST óptimo | $431 millones |
| Ahorro con MST | $793 millones |
| Subestaciones críticas | Ninguna |

## Algoritmos implementados

- Kruskal con Union-Find — O(E log E)
- Prim con min-heap — O(E log V)
- Detección de nodos de articulación con DFS — O(V+E)
- BFS para redirección de energía tras fallos — O(V+E)

## Cómo ejecutar

### Simulador interactivo
Iniciar el servidor:
```bash
cd /workspaces/Red_electrica
python3 -m http.server 3000
```
Abrir el puerto 3000 en el navegador y hacer clic en app.html

### Simulación en terminal
```bash
cd src
python3 simulacion.py
```

### Tests de verificación
```bash
cd src
python3 ../tests/test_algoritmos.py
```

### Visualización estática
```bash
pip install matplotlib networkx
cd src
python3 visualizacion.py
```

## Requisitos

- Python 3.8+
- NetworkX
- Matplotlib
