# 1. Abre test_diccionario_ordenado.py (el que escribiste en la semana 10
#    contra la especificación, no contra el BST).
#
# 2. Cambia UNA SOLA LÍNEA:
#
#       # ANTES
#       from abb import ABB as DiccionarioOrdenado
#
#       # DESPUÉS
#       from avl import AVL as DiccionarioOrdenado
#
# 3. Ejecuta:  pytest test_diccionario_ordenado.py -v
#
# 4. No toques NADA más. Todas las pruebas deben pasar.
#
# 5. Ahora ejecuta la comparación:

import math, random, time
from abb import ABB
from avl import AVL

N = 5_000
print(f"{'Estructura':<12} {'Inserción ordenada':>20} {'Altura':>8} {'Búsquedas':>12}")

for nombre, Clase in [("BST", ABB), (u"AVL", AVL)]:
    arbol = Clase()
    inicio = time.perf_counter()
    for c in range(N):                       # ¡en orden: el peor caso!
        arbol.insertar(c)
    t_insercion = (time.perf_counter() - inicio) * 1000

    muestra = random.sample(range(N), 300)
    inicio = time.perf_counter()
    for c in muestra:
        arbol.contiene(c)
    t_busqueda = (time.perf_counter() - inicio) * 1000

    print(f"{nombre:<12} {t_insercion:>17.1f} ms {arbol.altura():>8} "
          f"{t_busqueda:>9.2f} ms")

print(f"\nAltura teórica ideal: {math.log2(N):.1f}")

# 6. Escribe en el historial del plan.md:
#
#    | Versión | Fecha | Cambio | Motivo |
#    |---------|-------|--------|--------|
#    | 2.0 | <fecha> | Implementación cambiada de BST a AVL | La implementación
#    |     |         |  anterior no garantizaba la complejidad O(log n)
#    |     |         |  declarada en el peor caso (inserción ordenada
#    |     |         |  degeneraba a O(n)). El spec.md NO cambió: el
#    |     |         |  contrato era correcto, la implementación no lo cumplía. |