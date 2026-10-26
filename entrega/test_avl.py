# Código base — Semana 12
# Fuente: 02-Momento-2-Disciplina-y-jerarquia/12-Semana-12-Arboles-AVL/02-guia-de-laboratorio.html

from avl import AVL


def test_caso_LL():
    """Inserción izquierda-izquierda: una rotación derecha.
    30, 20, 10  ->  raíz debe quedar en 20"""
    a = AVL()
    for c in [30, 20, 10]:
        a.insertar(c)
    assert a.raiz.dato == 20
    assert a.raiz.izquierdo.dato == 10
    assert a.raiz.derecho.dato == 30
    assert a.altura() == 1
    assert a.es_avl_valido()


def test_caso_RR():
    """Inserción derecha-derecha: una rotación izquierda.
    10, 20, 30  ->  raíz debe quedar en 20"""
    a = AVL()
    for c in [10, 20, 30]:
        a.insertar(c)
    assert a.raiz.dato == 20
    assert a.altura() == 1
    assert a.es_avl_valido()


def test_caso_LR():
    """Zigzag izquierda-derecha: dos rotaciones.
    30, 10, 20  ->  raíz debe quedar en 20"""
    a = AVL()
    for c in [30, 10, 20]:
        a.insertar(c)
    assert a.raiz.dato == 20
    assert a.raiz.izquierdo.dato == 10
    assert a.raiz.derecho.dato == 30
    assert a.es_avl_valido()


def test_caso_RL():
    """Zigzag derecha-izquierda: dos rotaciones.
    10, 30, 20  ->  raíz debe quedar en 20"""
    a = AVL()
    for c in [10, 30, 20]:
        a.insertar(c)
    assert a.raiz.dato == 20
    assert a.es_avl_valido()


def test_insercion_ordenada_no_degenera():
    """LA PRUEBA QUE JUSTIFICA TODA LA SEMANA.

    Con un BST, insertar 1..1000 en orden da altura 999.
    Con un AVL debe dar aproximadamente log2(1000) ~= 10.
    """
    import math
    N = 1000
    a = AVL()
    for c in range(N):
        a.insertar(c)
    assert a.inorden() == list(range(N))
    assert a.es_avl_valido()
    # La cota teórica del AVL es 1,44 * log2(n)
    assert a.altura() <= 1.44 * math.log2(N) + 1


def test_eliminar_rebalancea():
    a = AVL()
    for c in [50, 30, 70, 20, 40, 60, 80, 10]:
        a.insertar(c)
    for c in [70, 80, 60]:
        a.eliminar(c)
        assert a.es_avl_valido(), f"quedó desbalanceado tras eliminar {c}"


def test_estres_aleatorio():
    """Miles de operaciones mezcladas: el invariante nunca se rompe."""
    import random
    random.seed(7)
    a = AVL()
    presentes = set()
    for _ in range(2000):
        if random.random() < 0.65 or not presentes:
            c = random.randint(0, 500)
            a.insertar(c)
            presentes.add(c)
        else:
            c = random.choice(list(presentes))
            a.eliminar(c)
            presentes.discard(c)
        assert a.es_avl_valido()
    assert a.inorden() == sorted(presentes)
