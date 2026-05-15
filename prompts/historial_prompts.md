# Historial de Prompts con IA

**Estudiante:** Pedro Díaz — Código 96000
**Materia:** Estructura de Datos — UCC 2026
**Herramienta:** Claude (Anthropic) — Sonnet 4.6

---

## Etapa 1 — Definición del problema

### Prompt 1 — Refinamiento del problema
**Objetivo:** Mejorar la redacción sin cambiar la intención original

**Prompt enviado:**
Tengo el siguiente problema que quiero resolver como proyecto académico.
Por favor ayúdame a reformularlo de forma más clara, precisa y
estructurada, sin cambiar la intención original: El problema consiste
en encontrar la manera más eficiente y económica de conectar varias
subestaciones eléctricas dentro de una red inteligente.

**Qué generó la IA:**
Versión estructurada con contexto, definición formal, actores afectados,
solución propuesta y criterio de éxito.

**Por qué usé este prompt:**
Tenía claro el problema pero necesitaba expresarlo técnicamente antes
de empezar a programar.

**Qué cambié:**
Eliminé actores que no eran relevantes para el contexto académico.

---

## Etapa 2 — Modelado del grafo

### Prompt 2 — Generación de la red
**Objetivo:** Crear el grafo base de la red eléctrica

**Prompt enviado:**
Necesito generar una red eléctrica con 15 subestaciones S1-S15 y 25
líneas de transmisión con pesos aleatorios entre 10 y 100 millones de
pesos. Represéntala como lista de adyacencia. Asegúrate de que el
grafo sea conexo y el código esté comentado.

**Qué generó la IA:**
grafo.py con árbol generador aleatorio más aristas adicionales hasta
completar 25 líneas usando random.seed(42).

**Por qué usé este prompt:**
Necesitaba una red de ejemplo con los parámetros que pedía el enunciado.

**Error crítico que detecté y corregí:**
Al ejecutar encontré que S11 solo tenía una conexión hacia S10.
Resultado al verificar: NODO CON UNA SOLA CONEXION: S11
Lo corregí agregando lógica que garantiza mínimo 2 conexiones por nodo.

---

### Prompt 3 — Justificación de estructura de datos
**Objetivo:** Entender y justificar la elección de lista de adyacencia

**Prompt enviado:**
Tengo un grafo ponderado no dirigido con 15 nodos y 25 aristas.
Es mejor usar lista de adyacencia o matriz de adyacencia para
implementar Kruskal y Prim?

**Qué generó la IA:**
Lista ocupa O(V+E) contra O(V2) de la matriz. Para grafos dispersos
la lista es más eficiente.

**Por qué usé este prompt:**
Necesitaba justificar técnicamente la decisión para el documento de
análisis.

---

## Etapa 3 — Algoritmos MST

### Prompt 4 — Implementación de Kruskal
**Objetivo:** Implementar el primer algoritmo MST

**Prompt enviado:**
Implementa el algoritmo de Kruskal en Python para encontrar el MST
de un grafo ponderado no dirigido. Usa Union-Find con compresión de
caminos y unión por rango. Retorna las aristas del MST y el costo total.

**Qué generó la IA:**
kruskal.py con ordenamiento de aristas y uso de Union-Find.

**Por qué usé este prompt:**
Kruskal es el algoritmo central del proyecto.

**Qué verifiqué:**
Que el MST tuviera exactamente 14 aristas y que el costo coincidiera
con el resultado de Prim.

---

### Prompt 5 — Implementación de Union-Find
**Objetivo:** Implementar la estructura auxiliar de Kruskal

**Prompt enviado:**
Implementa Union-Find con compresión de caminos y unión por rango
en Python para detectar si dos nodos pertenecen al mismo componente.

**Qué generó la IA:**
union_find.py con métodos find con compresión de caminos y union
con unión por rango.

**Por qué usé este prompt:**
Sin Union-Find, Kruskal tendría que hacer BFS para detectar ciclos
lo que lo haría mucho más lento.

**Qué revisé línea por línea:**
La compresión de caminos: si el padre de un nodo no es él mismo,
llama find recursivamente y asigna el resultado directo. Esto hace
que en la siguiente búsqueda el nodo apunte directamente a la raíz.

---

### Prompt 6 — Implementación de Prim
**Objetivo:** Segundo algoritmo MST para verificación cruzada

**Prompt enviado:**
Implementa el algoritmo de Prim en Python usando heapq para encontrar
el MST del mismo grafo. Retorna las aristas y el costo total para
verificar que coincide con Kruskal.

**Qué generó la IA:**
prim.py con min-heap usando heapq empezando desde S1.

**Por qué usé este prompt:**
Implementé Prim específicamente para verificar Kruskal.

**Resultado de la verificación:**
Kruskal: $431M — Prim: $431M — Coinciden.

---

## Etapa 4 — Detección de puntos críticos

### Prompt 7 — Nodos de articulación
**Objetivo:** Identificar subestaciones cuya falla desconecta la red

**Prompt enviado:**
Escribe en Python una función que detecte todos los nodos de
articulación de un grafo no dirigido usando DFS con valores disc y low.

**Qué generó la IA:**
articulacion.py con DFS recursivo que calcula disc y low por nodo.

**Por qué usé este prompt:**
El enunciado pedía identificar subestaciones críticas.

**Resultado antes y después de corregir el grafo:**
Antes: subestaciones críticas = S10
Después de garantizar mínimo 2 conexiones: ninguna subestación crítica.

---

## Etapa 5 — Simulación de fallos

### Prompt 8 — Simulación y BFS
**Objetivo:** Implementar fallo y redirección de energía

**Prompt enviado:**
Escribe una función que elimine una arista del grafo, recalcule el
MST sin ella y encuentre la ruta alternativa con BFS entre los nodos
afectados.

**Qué generó la IA:**
simulacion.py con simular_fallo, bfs_ruta y bloque principal.

**Por qué usé este prompt:**
Esta funcionalidad es el corazón de la resiliencia de la red.

**Resultado de la ejecución:**
Costo MST Kruskal: $431 millones
Costo MST Prim: $431 millones
Verificación: Coinciden
Subestaciones críticas: ninguna
Fallo en S1-S2: red sigue conectada
Nuevo costo MST: $471 millones
Ruta alternativa: S1 a S4 a S3 a S2

**Lo que entendí:**
El MST sube de $431M a $471M porque al eliminar S1-S2 el algoritmo
usa rutas más largas. La diferencia de $40M es el costo real del fallo.

---

## Etapa 6 — Visualización estática

### Prompt 9 — Imágenes PNG
**Objetivo:** Generar visualización compatible con Codespaces

**Prompt enviado:**
Usando NetworkX y Matplotlib visualiza la red eléctrica. MST en verde,
no-MST en gris punteado, nodos críticos en rojo. Guarda como PNG.

**Qué generó la IA:**
visualizacion.py con matplotlib.use Agg generando dos imágenes PNG.

**Error que corregí:**
La IA generó plt.show() que fallaba. Lo reemplacé por plt.savefig()
después de agregar matplotlib.use Agg al inicio del archivo.

---

## Etapa 7 — Interfaz interactiva

### Prompt 10 — app.html
**Objetivo:** Simulador interactivo en tiempo real en el navegador

**Prompt enviado:**
Construye una interfaz HTML interactiva con Canvas para el simulador.
Implementa Kruskal y BFS en JavaScript. Permite simular fallos en
líneas y nodos. Diseño Carbon Dark con panel de métricas y log.

**Qué generó la IA:**
app.html completo con todos los algoritmos en JavaScript y panel lateral.

**Por qué usé este prompt:**
La visualización PNG no cumplía RNF-02 que exige simulación en tiempo real.

**Errores que identifiqué y corregí:**
1. Valores incorrectos — actualicé con datos reales de grafo.py
2. Botón fijo en S10 — lo cambié para cualquier nodo seleccionado
3. Sin restaurar nodo — implementé clic sobre nodo eliminado
4. Nodos fijos — agregué arrastre con mouse
5. Conflicto de eventos — separé lógica de arrastre y clic

---

## Etapa 8 — Navegación y documentación

### Prompt 11 — index.html y viewer.html
**Objetivo:** Navegación profesional del proyecto

**Prompt enviado:**
Crea una página principal Carbon Dark como índice con links a todos
los archivos y métricas. También un visor de archivos py y md con
resaltado de sintaxis sin caracteres mal codificados.

**Qué generó la IA:**
index.html con diseño Carbon Dark y viewer.html con resaltado de sintaxis.

**Error que corregí:**
Caracteres mal codificados. Lo resolví con meta charset UTF-8.

---

## Resultado final del proyecto

Archivos Python: 7 módulos en src
Tests: 3 pruebas en test_algoritmos.py
Costo MST: $431 millones
Costo red completa: $1.224 millones
Ahorro: $793 millones
Subestaciones críticas: Ninguna
Interfaz interactiva: app.html funcional
Imágenes: red_normal.png y red_fallo_S1_S2.png
