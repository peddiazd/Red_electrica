# Documento de Análisis Técnico

**Estudiante:** Pedro Díaz
**Código:** 96000
**Materia:** Estructura de Datos — Universidad Cooperativa de Colombia 2026
**Docente:** Diego León Arcila Herrera

---

## 4.1 Definición del problema

El problema consiste en encontrar la manera más eficiente y económica
de conectar varias subestaciones eléctricas dentro de una red
inteligente. Cada conexión tiene un costo de instalación diferente
medido en millones de pesos, entonces la idea es usar algoritmos que
permitan construir una red funcional gastando lo menos posible y
evitando conexiones innecesarias.

Esto afecta principalmente a las empresas de energía y a las personas
que dependen del servicio eléctrico, porque una mala distribución puede
generar costos altos, desperdicio de recursos o apagones cuando ocurre
una falla en alguna línea. El impacto es tanto económico como operativo:
económico porque instalar cables innecesarios desperdicia millones de
pesos, y operativo porque una red sin rutas alternativas es vulnerable
a cualquier fallo.

La solución implementada es un simulador que construye la red más
económica posible usando algoritmos de Árbol de Expansión Mínima, y
que ante cualquier fallo puede redirigir automáticamente la energía
buscando rutas alternativas.

---

## 4.2 Justificación de la estructura de datos

Se modeló la red eléctrica como un grafo ponderado no dirigido donde
cada subestación es un nodo y cada línea de transmisión es una arista
con un peso que representa el costo de instalación en millones de pesos.

Se eligió esta estructura porque:
- Cada subestación se relaciona con varias otras sin jerarquía fija
- Las conexiones funcionan en ambos sentidos: la energía fluye de S1
  a S2 igual que de S2 a S1
- Los costos son diferentes entre conexiones, por lo que se necesitan
  pesos en las aristas
- El objetivo es minimizar el peso total: problema de MST

Se eligió lista de adyacencia sobre matriz de adyacencia porque el
grafo es disperso: tiene 25 aristas de 105 posibles, solo el 24%.
La lista ocupa O(V+E) igual a O(40) posiciones en memoria contra
O(V2) igual a O(225) de la matriz. Además cuando los algoritmos
recorren los vecinos de un nodo, con lista de adyacencia se accede
solo a los vecinos reales. Con matriz habría que revisar las 15
celdas de cada fila aunque la mayoría fueran cero.

Se eligió esta estructura y no una alternativa porque:
- Un árbol no sirve: la red tiene conexiones múltiples entre nodos
  que no siguen jerarquía
- Una lista enlazada no puede representar relaciones muchos a muchos
- Una tabla hash no preserva la relación topológica entre nodos

---

## 4.3 Análisis de complejidad

Kruskal con Union-Find: temporal O(E log E), espacial O(V + E)
Prim con min-heap: temporal O(E log V), espacial O(V + E)
Nodos de articulación DFS: temporal O(V + E), espacial O(V)
BFS ruta alternativa: temporal O(V + E), espacial O(V)
Union-Find find/union: temporal O(alfa(V)) amortizado, espacial O(V)

Para nuestra red V=15 y E=25. El factor dominante es E log E en
Kruskal y E log V en Prim. Con estos valores ambos son prácticamente
instantáneos. La diferencia se vuelve relevante en redes grandes:
para 1000 subestaciones con 5000 conexiones, Kruskal necesitaría
aproximadamente 60000 operaciones y Prim aproximadamente 50000.

---

## 4.4 Requisitos funcionales

RF-01: Visualizar la red eléctrica con pesos en las conexiones
RF-02: Calcular y resaltar el MST usando Prim o Kruskal
RF-03: Mostrar el costo total del MST vs el costo de la red completa
RF-04: Simular el fallo de una línea y actualizar la visualización
RF-05: Identificar y resaltar las subestaciones de articulación
RF-06: Encontrar la ruta alternativa de menor costo tras un fallo

Estado de cumplimiento:
RF-01: Cumplido en app.html y visualizacion.py
RF-02: Cumplido en kruskal.py, prim.py y app.html
RF-03: Cumplido en simulacion.py y app.html
RF-04: Cumplido en simulacion.py y app.html
RF-05: Cumplido en articulacion.py y app.html
RF-06: Cumplido en simulacion.py y app.html

---

## 4.5 Requisitos no funcionales

RNF-01: El cálculo del MST debe completarse en menos de 2 segundos
para 50 nodos. Cumplido: para 15 nodos el cálculo es instantáneo.

RNF-02: La simulación de fallo debe actualizarse visualmente en
tiempo real. Cumplido: app.html recalcula el MST al instante al
hacer clic en cualquier línea o nodo.

RNF-03: El código debe documentar claramente qué algoritmo se usa
y por qué. Cumplido: todos los módulos tienen docstrings y comentarios.

RNF-04: La interfaz debe mostrar el MST con un color distinto al
grafo completo. Cumplido: MST en verde, no-MST en gris punteado,
ruta alternativa en amarillo, línea fallida en rojo.

---

## 4.6 Preguntas de reflexión

### Pregunta 1: ¿Cuándo preferirías Prim sobre Kruskal?

Kruskal trabaja de forma global: ordena todas las aristas por costo
y las agrega si no forman ciclos usando Union-Find. Es como revisar
todas las opciones disponibles de menor a mayor precio y elegir las
que no repiten una conexión ya existente.

Prim trabaja de forma local: empieza desde S1 y crece el árbol
agregando siempre el vecino más barato disponible usando un heap.
Es como expandir una red desde un punto central hacia afuera,
siempre eligiendo el siguiente paso más económico.

La característica que decide cuál usar es la densidad del grafo:
- Grafo disperso como el nuestro (25 de 105 aristas posibles, 24%):
  Kruskal es más eficiente porque ordena pocas aristas.
- Grafo denso (más del 50% de capacidad): Prim es mejor porque no
  necesita ordenar todas las aristas, solo explora vecinos del árbol.

En resumen: Kruskal selecciona aristas globalmente, Prim expande
nodos localmente. Para nuestra red dispersa Kruskal es la elección
correcta, aunque ambos producen el mismo resultado de $431M.

---

### Pregunta 2: ¿El MST es único?

En nuestra red el MST no es necesariamente único porque existen aristas
con el mismo peso. Por ejemplo S1-S2, S1-S8 y S10-S11 cuestan las
tres $13M.

Cuando Kruskal encuentra dos aristas con el mismo peso y debe elegir
una, cualquiera produce un MST válido con el mismo costo total de
$431M pero con diferentes conexiones incluidas.

La regla general es:
- Si todos los pesos son distintos: el MST es único.
- Si hay pesos repetidos: pueden existir múltiples MST válidos con
  el mismo costo total pero con aristas diferentes.

---

### Pregunta 3: ¿Cómo cambiaría el problema si algunas líneas son obligatorias?

Si una línea es obligatoria, Kruskal tendría que incluirla desde el
inicio aunque en ese momento no sea la siguiente en la lista ordenada.

Lo que cambia en el algoritmo:
- La arista obligatoria se agrega primero al MST de forma forzada
  antes de que Kruskal comience su proceso normal.
- Los nodos de esa arista quedan conectados desde el comienzo.
- Kruskal continúa normalmente con las demás aristas evitando ciclos.

El algoritmo pierde libertad para escoger conexiones óptimas porque
parte de la red ya está fija. Esto puede aumentar el costo total del
MST o hacer que aristas baratas queden descartadas porque formarían
ciclos con la conexión obligatoria.

En otras palabras, el MST dejaría de ser el árbol mínimo absoluto
y pasaría a ser el árbol mínimo posible respetando las restricciones.

---

### Pregunta 4: ¿Qué es un nodo de articulación y cómo lo detectaste?

Un nodo de articulación es una subestación que si se elimina hace que
la red se divida y algunas partes queden incomunicadas. Funciona como
un puente crítico dentro del sistema.

Se detectó con DFS usando dos valores por nodo:
- disc: el tiempo en que se descubrió el nodo durante el recorrido
- low: el nodo más antiguo al que puede llegar sin pasar por su padre

Si un nodo tiene un hijo en el DFS cuyo valor low es mayor o igual
al disc del padre, ese padre es un nodo de articulación porque el
hijo no tiene otra forma de llegar al resto del grafo sin pasar por él.

Evolución en este proyecto:
Inicialmente S10 era el único nodo de articulación porque S11 solo
tenía una conexión directa hacia él. Se corrigió el diseño en grafo.py
garantizando mínimo 2 conexiones por nodo. Después de esa corrección
el resultado fue un conjunto vacío: ninguna subestación es punto crítico.

---

### Pregunta 5: ¿Cómo verificaste que tu MST es el de menor costo?

Se verificó de tres formas:

1. Verificación cruzada entre algoritmos:
Kruskal y Prim produjeron el mismo costo total de $431M. Aunque
trabajan diferente, deben llegar al mismo costo mínimo. Esa
coincidencia confirmó que las implementaciones eran correctas.

2. Verificación de propiedades del MST con test_algoritmos.py:
- El MST tiene exactamente 14 aristas (N-1 para 15 nodos)
- No se forman ciclos gracias al Union-Find en Kruskal
- Todos los nodos quedan conectados

3. Comparación con el costo total de la red:
El MST cuesta $431M sobre un total de $1.224M, una reducción del
64.8%. Esta diferencia confirma que el algoritmo encontró una red
genuinamente optimizada.

---

### Pregunta 6: ¿La IA implementó correctamente el Union-Find?

La implementación estaba correcta. La lógica de find, union,
compresión de caminos y uso de rango estaba bien aplicada.

El rango sirve para mantener equilibrados los árboles dentro del
Union-Find. Cuando se unen dos conjuntos, el árbol más pequeño queda
debajo del más grande para evitar estructuras muy profundas. Esto
hace las búsquedas más rápidas porque evita cadenas largas de nodos.

La compresión de caminos en el método find hace que después de cada
búsqueda, todos los nodos del camino apunten directamente a la raíz.
Esto significa que la próxima búsqueda sobre esos nodos es instantánea.

No se encontraron errores graves. Se agregaron comentarios adicionales
para facilitar la comprensión durante la sustentación.

Si el Union-Find no tuviera compresión de caminos, el resultado final
del MST seguiría siendo exactamente el mismo. Lo que cambia es la
eficiencia: las búsquedas recorrerían árboles más profundos. La
compresión es una optimización de velocidad, no de resultado.
