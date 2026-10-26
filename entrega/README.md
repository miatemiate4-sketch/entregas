# Entrega — BST y AVL (Semana 11 + Semana 12)

Esta carpeta conserva el código base de Semana 12 (`avl.py`, `test_avl.py` y las tres plantillas) y agrega la implementación BST, pruebas, informe y experimento solicitados.

## Ejecutar

Requiere Python 3 y pytest:

```bash
python -m pip install pytest
pytest -v
python benchmark.py
```

`benchmark.py` carga 10.000 claves en orden y en orden aleatorio, mide la altura y el tiempo de 1.000 búsquedas, y muestra las rotaciones del AVL. Los tiempos varían entre equipos; las alturas son reproducibles con la semilla configurada.
