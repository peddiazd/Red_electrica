# AGENTS.md

## Proyecto
Simulador de Red Electrica Inteligente - UCC 2026

## Entorno
- Python 3.8+
- GitHub Codespaces
- Directorio: /workspaces/Red_electrica

## Estructura
- src/     codigo fuente
- tests/   pruebas
- docs/    documentacion e imagenes
- prompts/ historial de prompts

## Reglas
- snake_case para variables y funciones
- Docstring obligatorio en cada modulo
- No modificar random.seed(42) en grafo.py
- No cambiar datos de la red en app.html sin actualizar grafo.py
- No modificar tests/ sin confirmacion del estudiante
- Un commit por etapa completada

## Comandos
- Simulacion: cd src && python3 simulacion.py
- Tests: cd src && python3 ../tests/test_algoritmos.py
- Servidor: python3 -m http.server 3000
- Visualizacion: cd src && python3 visualizacion.py

## Prohibiciones
- No cambiar random.seed(42)
- No eliminar comentarios del codigo
- No modificar archivos fuera de src/ sin confirmacion
