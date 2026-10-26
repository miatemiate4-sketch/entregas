from bst import BST

def arbol_ejemplo():
    a = BST()
    for x in [50, 30, 70, 20, 40, 60, 80]:
        a.insertar(x)
    return a

def test_insertar_buscar_y_duplicados():
    a = BST()
    assert a.insertar(5)
    assert a.insertar(3)
    assert not a.insertar(5)
    assert a.contiene(3) and not a.contiene(99)
    assert a.inorden() == [3, 5]
    assert a.es_bst_valido()

def test_eliminar_hoja():
    a = arbol_ejemplo()
    a.eliminar(20)
    assert a.inorden() == [30, 40, 50, 60, 70, 80]
    assert a.es_bst_valido()

def test_eliminar_nodo_con_un_hijo():
    a = BST()
    for x in [50, 30, 20]:
        a.insertar(x)
    a.eliminar(30)
    assert a.inorden() == [20, 50]
    assert a.es_bst_valido()

def test_eliminar_raiz_con_dos_hijos_mantiene_bst():
    a = arbol_ejemplo()
    a.eliminar(50)
    assert a.inorden() == [20, 30, 40, 60, 70, 80]
    assert a.raiz.dato == 60
    assert a.es_bst_valido()
    assert len(a) == 6

def test_eliminar_no_existente():
    a = BST()
    a.insertar(1)
    try:
        a.eliminar(99)
    except KeyError:
        pass
    else:
        assert False, "debe lanzar KeyError"
