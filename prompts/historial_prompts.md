## Resultado de ejecución — simulacion.py

**Fecha:** 2026  
**Resultado:** Código ejecutado sin errores  

**Lo que observé:**
- Costo red completa: $1.255 millones
- Costo MST óptimo: $427 millones
- Ahorro: $828 millones
- Kruskal y Prim coinciden: ✓
- Subestación crítica encontrada: S10
- Fallo S1-S2: red sigue conectada, ruta alternativa S1→S4→S3→S2

**Lo que entendí:**
S10 es crítica porque es el único camino que tiene S11 para 
conectarse al resto de la red. S11 solo tiene una conexión y 
es precisamente con S10, lo que significa que si S10 falla, 
S11 queda completamente aislada sin ninguna ruta alternativa 
para recibir o enviar energía.

Que el MST cueste $427M en lugar de $1255M significa que no 
todas las conexiones de la red son necesarias para mantenerla 
operativa. La red completa tiene 25 líneas pero muchas de ellas 
crean rutas redundantes. El MST selecciona solo las 14 líneas 
más baratas que mantienen todas las subestaciones conectadas 
sin duplicar caminos. La diferencia de $828M representa el 
costo de esas conexiones redundantes que existen como respaldo 
pero no son indispensables para la conectividad básica.