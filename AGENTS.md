# AGENTS.md — Registro de uso de IA

## Herramienta utilizada
- **IA:** Claude (Anthropic)
- **Interfaz:** claude.ai
- **Modelo:** Claude Sonnet 4.6

---

## Etapa 1 — Diseño y modelado de la red

### Prompt usado
Generar una red eléctrica con 15 subestaciones (S1-S15) y 25 
líneas de transmisión con pesos aleatorios entre 10 y 100 
millones de pesos, representada como lista de adyacencia en 
Python. También se pidió justificación entre lista de adyacencia 
vs matriz de adyacencia.

### Qué generó la IA
Código funcional con dos pasos: un árbol generador aleatorio 
para garantizar conectividad y aristas adicionales hasta 
completar 25 líneas. También generó una comparación técnica 
justificando la lista de adyacencia para grafos dispersos.

### Qué revisé y corregí
Se revisó que el grafo generado fuera realmente conexo y que 
los pesos estuvieran dentro del rango establecido. La lógica 
de generación era correcta y no requirió correcciones mayores.

### Qué aprendí
Que la lista de adyacencia es más eficiente que la matriz para 
grafos dispersos porque ocupa O(V+E) memoria en lugar de O(V²), 
y permite recorrer solo los vecinos reales de cada nodo.

---

## Etapa 2 — Algoritmos MST

### Prompt usado
Implementar Kruskal con Union-Find con compresión de caminos y 
unión por rango. Implementar Prim con min-heap. Verificar que 
ambos producen el mismo costo total del MST.

### Qué generó la IA
Dos módulos independientes: kruskal.py y prim.py, cada uno 
retornando las aristas del MST y el costo total. También generó 
union_find.py con compresión de caminos y unión por rango.

### Qué revisé y corregí
Se verificó que la implementación del Union-Find aplicara 
correctamente la compresión de caminos en el método find y 
la unión por rango en el método union. La implementación estaba 
correcta. Se agregaron comentarios adicionales para facilitar 
la comprensión del código.

### Qué aprendí
Que aunque Kruskal y Prim trabajan de forma diferente, llegan 
al mismo costo mínimo. Kruskal selecciona aristas globalmente 
mientras Prim expande nodos localmente desde un punto inicial. 
La verificación cruzada entre ambos confirmó que las 
implementaciones eran correctas al coincidir en $427 millones.

---

## Etapa 3 — Detección de puntos críticos

### Prompt usado
Implementar detección de nodos de articulación usando DFS con 
valores disc y low para identificar subestaciones críticas cuya 
falla desconecta la red.

### Qué generó la IA
El módulo articulacion.py con DFS recursivo usando tiempo de 
descubrimiento y valor low para cada nodo. Retorna el conjunto 
de nodos de articulación del grafo.

### Qué revisé y corregí
Se verificó que el algoritmo manejara correctamente tanto el 
caso del nodo raíz (con más de un hijo en el DFS) como el caso 
de nodos internos (cuyo hijo no puede alcanzar un ancestro sin 
pasar por él). La lógica estaba correcta.

### Qué aprendí
Que S10 es la única subestación crítica porque S11 depende 
exclusivamente de ella para conectarse al resto de la red. 
Si S10 falla, S11 queda completamente aislada. Esto demuestra 
la importancia de identificar estos puntos antes de diseñar 
una red eléctrica real.

---

## Etapa 4 — Simulación de fallos

### Prompt usado
Implementar función que elimine una arista específica del grafo, 
recalcule el MST sin ella y encuentre una ruta alternativa con 
BFS entre los nodos afectados.

### Qué generó la IA
El módulo simulacion.py con tres funciones: simular_fallo que 
elimina la arista y recalcula el MST, bfs_ruta que encuentra 
la ruta alternativa de menor número de saltos, y el bloque 
principal que ejecuta todo el flujo.

### Qué revisé y corregí
Se verificó que la eliminación de la arista se aplicara 
correctamente tanto en la lista de aristas como en el diccionario 
del grafo para mantener consistencia. La implementación estaba 
correcta.

### Qué aprendí
Que cuando falla la línea S1-S2, la red sigue conectada porque 
existen rutas alternativas. El nuevo MST cuesta $467 millones, 
$40 millones más que el óptimo, y la ruta alternativa encontrada 
por BFS fue S1→S4→S3→S2. Esto demuestra la resiliencia del 
sistema ante fallos.

---

## Etapa 5 — Visualización

### Prompt usado
Visualizar la red eléctrica con NetworkX y Matplotlib guardando 
el resultado como imagen PNG para compatibilidad con Codespaces. 
Mostrar el MST en verde, conexiones no MST en gris punteado, 
subestaciones críticas en rojo y ruta alternativa en naranja.

### Qué generó la IA
El módulo visualizacion.py usando backend Agg de Matplotlib 
para evitar errores de display en Codespaces. Genera dos 
imágenes: red_normal.png con el MST óptimo y red_fallo_S1_S2.png 
con la simulación del fallo.

### Qué revisé y corregí
Se identificó que Matplotlib intentaba abrir una ventana gráfica 
lo cual no es compatible con Codespaces. Se agregó la línea 
matplotlib.use('Agg') antes de importar pyplot para resolver 
el problema. Las imágenes se guardaron correctamente en docs/.

### Qué aprendí
Que los entornos de desarrollo en la nube como Codespaces no 
tienen display gráfico y requieren backends alternativos para 
generar visualizaciones. La solución fue guardar las imágenes 
como archivos PNG en lugar de mostrarlas en pantalla.

---

## Etapa 6 — Documentación

### Prompt usado
Completar el documento de análisis con las secciones 4.1 a 4.6, 
incluyendo las seis preguntas de reflexión sobre los algoritmos 
implementados y el uso de la IA.

### Qué generó la IA
La estructura completa del documento de análisis con justificación 
de la estructura de datos, análisis de complejidad y respuestas 
a las seis preguntas de reflexión basadas en los resultados 
reales de la ejecución del simulador.

### Qué revisé y corregí
Las respuestas a las preguntas de reflexión fueron construidas 
en conjunto: primero el estudiante respondió con sus propias 
palabras y luego la IA agregó el complemento técnico. Las 
secciones 4.1 y 4.2 fueron redactadas directamente por el 
estudiante sin apoyo de la IA.

### Qué aprendí
Que documentar el proceso es tan importante como el código en 
sí. El AGENTS.md y el historial de prompts demuestran que el 
uso de la IA fue una herramienta de apoyo y no un reemplazo 
del pensamiento propio. Las decisiones clave del proyecto 
fueron tomadas por el estudiante.