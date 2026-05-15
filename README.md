# Simulador de Red Eléctrica Inteligente

**Universidad Cooperativa de Colombia — Estructura de Datos 2026**  
**Docente:** Diego León Arcila Herrera

## Descripción
Simulador de una red eléctrica inteligente que modela subestaciones 
como nodos y líneas de transmisión como aristas con pesos (costo de 
instalación en millones de pesos). Encuentra la red de distribución 
más económica usando algoritmos de Árbol de Expansión Mínima (MST) 
y simula fallos redirigiendo la energía.

## Algoritmos implementados
- Kruskal con Union-Find
- Prim con min-heap
- Detección de nodos de articulación con DFS
- BFS para redirección de energía tras fallos

## Estructura del proyecto
- `src/` — Código fuente de los algoritmos
- `tests/` — Casos de prueba
- `docs/` — Documento de análisis técnico
- `prompts/` — Historial de prompts con IA

## Requisitos
- Python 3.8+
- NetworkX
- Matplotlib

## Ejecución
```bash
python src/simulacion.py
```

## Estudiante
- **Nombre:** [Tu nombre]
- **Código:** [Tu código estudiantil]
- **Programa:** [Tu programa]
- **Semestre:** [Tu semestre]