# AGENTS.md — Registro de uso de Inteligencia Artificial

**Estudiante:** Pedro Díaz — Código 96000
**Materia:** Estructura de Datos — UCC 2026
**Herramienta:** Claude (Anthropic) — claude.ai — Modelo Sonnet 4.6

---

## Sobre este documento

Este archivo documenta de forma honesta cómo se usó la IA en cada
etapa del proyecto. El uso de IA fue una herramienta de apoyo, no un
reemplazo del pensamiento propio. Cada vez que la IA generó código o
texto, el estudiante lo revisó, lo ejecutó, identificó errores y tomó
decisiones de corrección. Las decisiones de diseño más importantes
fueron tomadas por el estudiante, no por la IA.

---

## Etapa 1 — Definición del problema

### Lo que hice primero
Antes de usar la IA escribí con mis propias palabras el problema:
encontrar la red más económica para conectar subestaciones eléctricas
y garantizar que ante un fallo la energía se pueda redirigir. Solo
después de tener esa versión propia usé la IA para refinarlo.

### Prompt usado
"Tengo el siguiente problema que quiero resolver como proyecto académico.
Por favor ayúdame a reformularlo de forma más clara, precisa y
estructurada, sin cambiar la intención original."

### Qué generó la IA
Una versión estructurada con contexto, definición formal, actores
afectados y criterio de éxito. Mantuvo la intención original pero le
dio más precisión técnica.

### Qué revisé y corregí
Verifiqué que la reformulación no cambiara el sentido. Ajusté la
sección de actores porque la IA incluyó roles que no eran relevantes
para el contexto del proyecto académico.

### Qué aprendí
Que definir el problema con claridad antes de codificar ahorra tiempo.
Esta reformulación me sirvió como referencia durante todo el proyecto.

---

## Etapa 2 — Modelado del grafo

### Archivo creado: src/grafo.py

### Prompt usado
"Necesito generar una red eléctrica con 15 subestaciones S1-S15 y 25
líneas de transmisión con pesos aleatorios entre 10 y 100 millones de
pesos. Represéntala como lista de adyacencia. Asegúrate de que el
grafo sea conexo y el código esté comentado."

### Qué generó la IA
Código con árbol generador aleatorio para garantizar conectividad y
aristas adicionales hasta completar 25 líneas con random.seed(42).

### Qué revisé y corregí
Al ejecutar detecté el error más importante del proyecto: S11 solo
tenía una conexión hacia S10. Si S10 fallaba, S11 quedaba completamente
aislada. Lo corregí agregando lógica que garantiza mínimo 2 conexiones
por nodo. Este fue el único error de diseño significativo que encontré
y corregí yo directamente.

### Qué aprendí
Que la lista de adyacencia es más eficiente que la matriz para grafos
dispersos: O(V+E) vs O(V²). Que en una red eléctrica real ninguna
subestación puede depender de una sola conexión.

---

## Etapa 3 — Union-Find y algoritmos MST

### Archivos creados: src/union_find.py, src/kruskal.py, src/prim.py

### Prompts usados
Para Union-Find: "Implementa Union-Find con compresión de caminos y
unión por rango en Python para detectar si dos nodos pertenecen al
mismo componente conectado."

Para Kruskal: "Implementa Kruskal en Python para el MST de un grafo
ponderado. Usa Union-Find. Retorna las aristas del MST y el costo total."

Para Prim: "Implementa Prim con heapq para el MST del mismo grafo.
Retorna las aristas y el costo total para verificar que coincide con
Kruskal."

### Qué generó la IA
Tres módulos funcionales con las implementaciones correctas. Union-Find
con compresión de caminos y unión por rango. Kruskal con ordenamiento
de aristas. Prim con min-heap.

### Qué revisé y corregí
Revisé Union-Find línea por línea para entender la compresión de
caminos antes de incluirlo. Agregué comentarios para poder explicarlo
en la sustentación. Ejecuté verificación cruzada: Kruskal y Prim
coincidieron en $431M confirmando que ambas implementaciones eran
correctas.

### Qué aprendí
Que Kruskal y Prim siempre llegan al mismo costo aunque trabajan
diferente. La compresión de caminos no cambia el resultado del MST,
solo la velocidad de las búsquedas futuras.

---

## Etapa 4 — Detección de nodos de articulación

### Archivo creado: src/articulacion.py

### Prompt usado
"Escribe en Python una función que detecte nodos de articulación usando
DFS con valores disc y low. Retorna los nodos cuya eliminación
desconecta el grafo."

### Qué generó la IA
El módulo con DFS recursivo que calcula disc y low por nodo aplicando
los dos casos: nodo raíz con más de un hijo, y nodo interno cuyo hijo
no alcanza un ancestro sin pasar por él.

### Qué revisé y corregí
Verifiqué que con la red original S10 apareciera como nodo crítico.
Después de corregir grafo.py para garantizar mínimo 2 conexiones, el
resultado fue un conjunto vacío: ninguna subestación crítica. La
corrección del grafo fue decisión propia, no de la IA.

### Qué aprendí
Que un nodo de articulación no es necesariamente el más conectado.
S10 tenía 4 conexiones pero era crítico porque S11 dependía solo de
él. Lo que importa es si los vecinos tienen rutas alternativas sin
pasar por ese nodo.

---

## Etapa 5 — Simulación de fallos y BFS

### Archivo creado: src/simulacion.py

### Prompt usado
"Escribe una función que elimine una arista del grafo, recalcule el
MST sin ella y encuentre la ruta alternativa con BFS. Si la red queda
desconectada debe indicarlo."

### Qué generó la IA
simulacion.py con simular_fallo, bfs_ruta y bloque principal que
ejecuta y muestra todos los resultados en consola.

### Qué revisé y corregí
Verifiqué que la eliminación se aplicara en ambas estructuras: lista
de aristas y diccionario del grafo. Si solo se eliminaba de una los
resultados eran inconsistentes. La implementación lo manejaba bien
pero lo verifiqué ejecutando paso a paso.

### Qué aprendí
Cuando falla S1-S2, el nuevo MST cuesta $471M — $40M más que el
óptimo de $431M. La ruta alternativa fue S1 a S4 a S3 a S2. Esto
demuestra que la red absorbe fallos con un costo adicional manejable.

---

## Etapa 6 — Visualización estática

### Archivo creado: src/visualizacion.py

### Prompt usado
"Usando NetworkX y Matplotlib visualiza la red eléctrica. MST en verde,
no-MST en gris punteado, nodos críticos en rojo. Guarda como PNG
porque Codespaces no tiene display gráfico."

### Qué generó la IA
visualizacion.py con backend Agg generando red_normal.png y
red_fallo_S1_S2.png con la ruta alternativa en naranja.

### Qué revisé y corregí
La IA generó plt.show() que fallaba en Codespaces. Identifiqué el
error y apliqué matplotlib.use('Agg') antes de importar pyplot.

### Qué aprendí
Los entornos cloud no tienen display gráfico. Agg genera imágenes en
memoria sin necesitar ventana. Este problema no aparece en desarrollo
local.

---

## Etapa 7 — Interfaz interactiva

### Archivo creado: app.html

### Prompt usado
"Construye una interfaz HTML interactiva con Canvas para el simulador.
Implementa Kruskal y BFS en JavaScript. Permite simular fallos en
líneas y nodos. Muestra rutas alternativas en tiempo real. Diseño
Carbon Dark con panel de métricas y log del sistema."

### Qué generó la IA
HTML completo con Kruskal, Prim, DFS y BFS en JavaScript. Panel
lateral con métricas, leyenda, log y controles de simulación.

### Qué revisé y corregí
Identifiqué y corregí cinco problemas probando la interfaz:
1. Valores de costo incorrectos — actualicé con datos reales de grafo.py
2. Botón de fallo fijo en S10 — lo cambié para cualquier nodo seleccionado
3. Sin forma de restaurar nodo eliminado — implementé clic para restaurar
4. Nodos sin movimiento — agregué arrastre con mouse
5. Conflicto mouseup y click — separé lógica de arrastre y clic

### Qué aprendí
Reimplementar algoritmos en otro lenguaje obliga a entenderlos a fondo.
Las interfaces tienen problemas que solo aparecen con uso real.

---

## Etapa 8 — Navegación y visor de archivos

### Archivos creados: index.html, viewer.html

### Prompt usado
"Crea una página principal Carbon Dark como índice del proyecto con
links a todos los archivos y métricas. También un visor de archivos
.py y .md con resaltado de sintaxis y sin caracteres mal codificados."

### Qué generó la IA
index.html con diseño Carbon Dark, métricas y links a todos los
archivos. viewer.html con resaltado de sintaxis Python y renderizado
Markdown.

### Qué revisé y corregí
Los archivos mostraban caracteres como elÃ©ctrico en lugar de
eléctrico. Lo resolví usando entidades HTML y verificando meta charset
UTF-8 en todos los archivos.

### Qué aprendí
El encoding UTF-8 debe declararse explícitamente al servir texto en
HTTP para evitar caracteres mal codificados.

---

## Reflexión final

Usar Claude fue útil pero requirió trabajo crítico constante. El error
más significativo fue S11 con una sola conexión — un error de diseño
que identifiqué yo analizando los resultados del programa. La IA fue
útil para generar estructura base, explicar conceptos y acelerar la
documentación. No fue suficiente sin revisión para tomar decisiones
de diseño o garantizar coherencia entre Python y JavaScript.
