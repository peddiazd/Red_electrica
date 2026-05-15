# Documento de Análisis Técnico

## 4.1 Definición del problema
El problema consiste en encontrar la manera más eficiente y 
económica de conectar varias subestaciones eléctricas dentro 
de una red inteligente. Cada conexión tiene un costo de 
instalación diferente medido en millones de pesos, entonces 
la idea es usar algoritmos que permitan construir una red 
funcional gastando lo menos posible y evitando conexiones 
innecesarias.

Esto afecta principalmente a las empresas de energía y a las 
personas que dependen del servicio eléctrico, porque una mala 
distribución puede generar costos altos, desperdicio de recursos 
o apagones cuando ocurre una falla en alguna línea.

## 4.2 Justificación de la estructura de datos
El peso de cada línea representa el costo de instalación en 
millones de pesos. Se eligió esta representación porque el 
objetivo principal de la red es encontrar la forma más económica 
de conectar todas las subestaciones sin gastar recursos de más. 
De esta manera, el algoritmo puede analizar qué conexiones son 
más baratas y construir una red eficiente reduciendo costos 
innecesarios.

Se usó un grafo ponderado no dirigido porque:
- Cada subestación es un nodo
- Cada línea de transmisión es una arista con peso (costo)
- Las conexiones no tienen dirección: la energía puede fluir 
  en ambos sentidos
- Se necesita el menor peso total posible: problema de MST

Se eligió lista de adyacencia sobre matriz de adyacencia porque 
el grafo es disperso: tiene 25 aristas de 105 posibles (24%). 
La lista ocupa O(V+E) memoria contra O(V²) de la matriz, y 
permite recorrer solo los vecinos reales de cada nodo.
## 4.3 Análisis de complejidad

| Algoritmo | Complejidad temporal | Complejidad espacial
| Kruskal con Union-Find | O(E log E) | O(V + E) |
| Prim con min-heap | O(E log V) | O(V + E) |
| Nodos de articulación DFS | O(V + E) | O(V) |
| BFS ruta alternativa | O(V + E) | O(V) |
| Union-Find find/union | O(α(V)) amortizado | O(V) |

Para nuestra red: V=15, E=25. El factor dominante es E log E 
en Kruskal y E log V en Prim. Con estos valores ambos son 
prácticamente instantáneos, pero en redes de cientos de 
subestaciones la diferencia entre algoritmos se vuelve relevante.

## 4.4 Requisitos funcionales

- RF-01: Visualizar la red eléctrica con pesos en las conexiones
- RF-02: Calcular y resaltar el MST usando Prim o Kruskal
- RF-03: Mostrar el costo total del MST vs el costo total 
  de la red completa
- RF-04: Simular el fallo de una línea y actualizar 
  la visualización
- RF-05: Identificar y resaltar las subestaciones de articulación
- RF-06: Encontrar la ruta alternativa de menor costo 
  tras un fallo

## 4.5 Requisitos no funcionales

- RNF-01: El cálculo del MST debe completarse en menos de 
  2 segundos para 50 nodos
- RNF-02: La simulación de fallo debe actualizarse 
  visualmente en tiempo real
- RNF-03: El código debe documentar claramente qué algoritmo 
  se usa y por qué
- RNF-04: La interfaz debe mostrar el MST con un color 
  distinto al grafo completo

## 4.6 Preguntas de reflexión
### Pregunta 1: ¿Cuándo preferirías Prim sobre Kruskal?

Kruskal trabaja de forma global: ordena todas las aristas por costo 
y las agrega si no forman ciclos usando Union-Find. Es como armar 
grupos separados y luego unirlos.

Prim trabaja de forma local: empieza desde S1 y crece el árbol 
agregando siempre el vecino más barato disponible usando un heap.

La característica que decide cuál usar es la densidad del grafo:
- Grafo disperso (como el nuestro, 25 de 105 aristas posibles): 
  Kruskal es más eficiente porque ordena pocas aristas.
- Grafo denso (muchas aristas): Prim es mejor porque solo explora 
  vecinos sin necesidad de ordenar todas las aristas.

En resumen: Kruskal selecciona aristas, Prim expande nodos.

### Pregunta 2: ¿El MST es único?

En nuestra red el MST no es necesariamente único porque existen 
aristas con el mismo peso. Por ejemplo S1-S2, S1-S8 y S10-S11 
cuestan las tres $13M.

Cuando Kruskal encuentra dos aristas con el mismo peso y debe 
elegir una, cualquiera de las dos produce un MST válido con el 
mismo costo total de $427M pero con diferentes conexiones.

La regla general es:
- Si todos los pesos son distintos: el MST es único.
- Si hay pesos repetidos: pueden existir múltiples MST válidos 
  con el mismo costo total pero con aristas diferentes.
  
### Pregunta 3: ¿Cómo cambiaría el problema si algunas líneas 
son obligatorias?

Si una línea es obligatoria, como S13-S14 de $10M, Kruskal 
tendría que incluirla desde el inicio aunque no sea la opción 
más económica en ese momento.

Lo que cambia:
- La arista obligatoria se agrega primero al MST de forma forzada.
- S13 y S14 quedan conectados desde el comienzo.
- Kruskal continúa normalmente con las demás aristas evitando ciclos.

El algoritmo pierde libertad para escoger conexiones óptimas 
porque parte de la red ya está fija. Esto puede aumentar el 
costo total del MST o hacer que algunas aristas baratas queden 
descartadas porque formarían ciclos con la conexión obligatoria.

En otras palabras, el MST dejaría de ser el árbol mínimo 
absoluto y pasaría a ser el árbol mínimo posible respetando 
las conexiones obligatorias.

### Pregunta 4: ¿Qué es un nodo de articulación y cómo lo detectaste?

Un nodo de articulación es una subestación que si se elimina 
hace que la red se divida y algunas partes queden incomunicadas. 
Funciona como un puente crítico dentro del sistema.

En nuestra red S10 es la única subestación crítica. Mirando sus 
conexiones: S4($74M), S11($13M), S8($45M), S15($56M). S11 solo 
tiene una conexión y es precisamente con S10, lo que la hace 
completamente dependiente de ella. Si S10 falla, S11 queda 
aislada sin ninguna ruta alternativa.

Técnicamente lo detectamos con DFS usando dos valores por nodo:
- disc: el tiempo en que se descubrió el nodo durante el recorrido
- low: el nodo más antiguo al que puede llegar sin pasar por su padre

Si un nodo tiene un hijo en el DFS cuyo valor low es mayor o 
igual al disc del nodo padre, significa que ese hijo no tiene 
otra forma de llegar al resto del grafo sin pasar por el padre. 
Ese padre es entonces un nodo de articulación.

### Pregunta 5: ¿Cómo verificaste que tu MST es el de menor costo?

Verificamos el MST de dos formas:

1. Comparando Kruskal y Prim: ambos algoritmos producieron el 
   mismo costo total de $427M. Aunque trabajan diferente, deben 
   llegar al mismo costo mínimo. Esa coincidencia confirmó que 
   la solución era correcta.

2. Verificando propiedades del MST con el test_algoritmos.py:
   - El MST tiene exactamente N-1 aristas (14 aristas para 15 nodos)
   - No se forman ciclos gracias al Union-Find en Kruskal
   - Todos los nodos quedan conectados

El caso de prueba principal fue ejecutar ambos algoritmos sobre 
la misma red de 15 subestaciones y 25 líneas, y verificar que:
- La red quedara completamente conectada
- El costo fuera $427M en ambos casos
- El costo del MST ($427M) fuera menor que el costo total 
  de la red completa ($1255M)

### Pregunta 6: ¿La IA implementó correctamente el Union-Find?

La implementación estaba correcta. La lógica de find, union, 
compresión de caminos y uso de rango estaba bien aplicada 
para el problema del MST.

El rango sirve para mantener equilibrados los árboles dentro 
del Union-Find. Cuando se unen dos conjuntos, el árbol más 
pequeño queda debajo del más grande para evitar estructuras 
muy profundas. Esto hace las búsquedas más rápidas porque 
evita formar cadenas largas de nodos.

No se encontraron errores graves de funcionamiento. Lo único 
que se mejoraría sería agregar más comentarios y validaciones 
para hacer el código más fácil de entender y mantener, pero 
a nivel algorítmico funcionaba correctamente.

Si el Union-Find no tuviera compresión de caminos, el resultado 
final del MST seguiría siendo correcto pero el algoritmo sería 
más lento. Las búsquedas recorrerían árboles más profundos. 
La compresión hace que los nodos apunten directamente a la raíz 
después de cada búsqueda, reduciendo el tiempo de ejecución 
en grafos grandes. No afecta la exactitud, solo la eficiencia.