"""Experimento reproducible de los cuatro escenarios solicitados."""
import random
import time
from bst import BST
from avl import AVL

N = 10_000
BUSQUEDAS = 1_000
SEMILLA = 2026

def medir(Clase, datos, consultas):
    arbol = Clase()
    inicio = time.perf_counter()
    for x in datos:
        arbol.insertar(x)
    ms_insercion = (time.perf_counter() - inicio) * 1000
    inicio = time.perf_counter()
    for x in consultas:
        arbol.contiene(x)
    ms_busqueda = (time.perf_counter() - inicio) * 1000
    return arbol, ms_insercion, ms_busqueda

def main():
    rng = random.Random(SEMILLA)
    ordenados = list(range(1, N + 1))
    desordenados = ordenados.copy()
    rng.shuffle(desordenados)
    consultas = rng.sample(ordenados, BUSQUEDAS)
    resultados = []
    for nombre, Clase, datos in [
        ("BST ordenado", BST, ordenados),
        ("BST desordenado", BST, desordenados),
        ("AVL ordenado", AVL, ordenados),
        ("AVL desordenado", AVL, desordenados),
    ]:
        arbol, t_ins, t_bus = medir(Clase, datos, consultas)
        rot = getattr(arbol, "rotaciones", 0)
        resultados.append((nombre, arbol.altura(), t_ins, t_bus, rot))
        print(f"{nombre}|{arbol.altura()}|{t_ins:.3f}|{t_bus:.3f}|{rot}")
        if isinstance(arbol, AVL):
            assert arbol.es_avl_valido()
        else:
            assert arbol.es_bst_valido()
    print(f"N={N}; busquedas={BUSQUEDAS}; semilla={SEMILLA}")
if __name__ == "__main__":
    main()
