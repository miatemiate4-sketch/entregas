"""Árbol binario de búsqueda (BST/ABB), sin balance automático."""
class NodoBST:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.raiz = None
        self._tamaño = 0

    def __len__(self):
        return self._tamaño

    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = NodoBST(clave)
            self._tamaño = 1
            return True
        actual = self.raiz
        while True:
            if clave == actual.dato:
                return False
            if clave < actual.dato:
                if actual.izquierdo is None:
                    actual.izquierdo = NodoBST(clave)
                    self._tamaño += 1
                    return True
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = NodoBST(clave)
                    self._tamaño += 1
                    return True
                actual = actual.derecho

    def contiene(self, clave):
        actual = self.raiz
        while actual is not None:
            if clave == actual.dato:
                return True
            actual = actual.izquierdo if clave < actual.dato else actual.derecho
        return False

    def eliminar(self, clave):
        """Elimina hoja, nodo con un hijo o nodo con dos hijos; falta -> KeyError."""
        padre = None
        actual = self.raiz
        while actual is not None and actual.dato != clave:
            padre = actual
            actual = actual.izquierdo if clave < actual.dato else actual.derecho
        if actual is None:
            raise KeyError(clave)

        # Caso 3: dos hijos. Copiar el sucesor inorden (mínimo del subárbol derecho)
        # y luego eliminar ese sucesor, que como máximo tiene un hijo derecho.
        if actual.izquierdo is not None and actual.derecho is not None:
            padre_suc = actual
            sucesor = actual.derecho
            while sucesor.izquierdo is not None:
                padre_suc = sucesor
                sucesor = sucesor.izquierdo
            actual.dato = sucesor.dato
            padre, actual = padre_suc, sucesor

        # En este punto el nodo tiene cero o un hijo.
        hijo = actual.izquierdo if actual.izquierdo is not None else actual.derecho
        if padre is None:
            self.raiz = hijo
        elif padre.izquierdo is actual:
            padre.izquierdo = hijo
        else:
            padre.derecho = hijo
        self._tamaño -= 1

    def inorden(self):
        resultado, pila, actual = [], [], self.raiz
        while pila or actual is not None:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierdo
            actual = pila.pop()
            resultado.append(actual.dato)
            actual = actual.derecho
        return resultado

    def altura(self):
        """Altura en aristas: árbol vacío=-1, hoja=0. Iterativa para evitar límite recursivo."""
        if self.raiz is None:
            return -1
        max_altura = -1
        pila = [(self.raiz, 0)]
        while pila:
            nodo, h = pila.pop()
            max_altura = max(max_altura, h)
            if nodo.izquierdo is not None: pila.append((nodo.izquierdo, h+1))
            if nodo.derecho is not None: pila.append((nodo.derecho, h+1))
        return max_altura

    def es_bst_valido(self):
        pila = []
        actual = self.raiz
        anterior = None
        hay_anterior = False
        while pila or actual is not None:
            while actual is not None:
                pila.append(actual); actual = actual.izquierdo
            actual = pila.pop()
            if hay_anterior and not (anterior < actual.dato):
                return False
            anterior, hay_anterior = actual.dato, True
            actual = actual.derecho
        return True
