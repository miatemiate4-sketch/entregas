# Código base — Semana 12
# Fuente: 02-Momento-2-Disciplina-y-jerarquia/12-Semana-12-Arboles-AVL/02-guia-de-laboratorio.html

class NodoAVL:
    """Nodo que almacena su propia altura.

    Si tuvieras que calcular la altura recorriendo el subárbol cada vez,
    el factor de balance costaría O(n) y el AVL perdería toda su ventaja.
    """

    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
        self.altura = 0          # una hoja tiene altura 0

    def __repr__(self):
        return f"NodoAVL({self.dato!r}, h={self.altura})"

class AVL:
    """Árbol Binario de Búsqueda autobalanceado (Adelson-Velsky y Landis).

    INVARIANTE AVL: para todo nodo n, |factor_balance(n)| <= 1

    Consecuencia: altura <= 1.44 * log2(n), es decir O(log n) GARANTIZADO,
    no solo en promedio.

    Complejidad:
        buscar   -> O(log n)   garantizado
        insertar -> O(log n)   garantizado (máximo 2 rotaciones)
        eliminar -> O(log n)   garantizado (hasta O(log n) rotaciones)

    Precio a pagar: cada inserción hace trabajo extra para mantener el
    balance. Si tus datos llegan ya aleatorizados y no necesitas la
    garantía del peor caso, un BST simple es más rápido en la práctica.
    """

    def __init__(self):
        self.raiz = None
        self._tamaño = 0
        self.rotaciones = 0

    def __len__(self):
        return self._tamaño

    # ---------- auxiliares de altura ----------

    def _altura(self, nodo):
        """O(1) porque la altura está almacenada."""
        return -1 if nodo is None else nodo.altura

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.izquierdo),
                              self._altura(nodo.derecho))

    def _factor_balance(self, nodo):
        if nodo is None:
            return 0
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    # ---------- rotaciones ----------

    def _rotar_derecha(self, z):
        self.rotaciones += 1
        """Rotación simple a la derecha. Devuelve la nueva raíz del subárbol.

              z                y
             / \             /   \
            y   D    =>      x     z
           / \                   / \
          x   C                 C   D

        El subárbol C cambia de padre: era el derecho de y,
        pasa a ser el izquierdo de z.
        """
        y = z.izquierdo
        c = y.derecho

        y.derecho = z
        z.izquierdo = c

        # ORDEN CRÍTICO: primero z (que ahora está abajo), después y
        self._actualizar_altura(z)
        self._actualizar_altura(y)
        return y

    def _rotar_izquierda(self, z):
        """Rotación simple a la izquierda."""
        self.rotaciones += 1
        y = z.derecho
        b = y.izquierdo
        y.izquierdo = z
        z.derecho = b
        # Primero actualizar el nodo que baja y luego la nueva raíz.
        self._actualizar_altura(z)
        self._actualizar_altura(y)
        return y

    # ---------- inserción con rebalanceo ----------

    def insertar(self, clave):
        antes = self._tamaño
        self.raiz = self._insertar(self.raiz, clave)
        return self._tamaño > antes

    def _insertar(self, nodo, clave):
        # 1. Inserción normal de BST
        if nodo is None:
            self._tamaño += 1
            return NodoAVL(clave)
        if clave < nodo.dato:
            nodo.izquierdo = self._insertar(nodo.izquierdo, clave)
        elif clave > nodo.dato:
            nodo.derecho = self._insertar(nodo.derecho, clave)
        else:
            return nodo                    # duplicado: no hacemos nada

        # 2. Actualizar la altura de este nodo
        self._actualizar_altura(nodo)

        # 3. Rebalancear si hace falta
        return self._rebalancear(nodo)

    def _rebalancear(self, nodo):
        """Aplica la rotación que corresponda según la tabla del paso 2."""
        fb = self._factor_balance(nodo)

        # Desbalance a la IZQUIERDA
        if fb > 1:
            if self._factor_balance(nodo.izquierdo) < 0:
                # CASO LR: primero endereza el hijo
                nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            # CASO LL (o LR ya enderezado)
            return self._rotar_derecha(nodo)

        # Desbalance a la DERECHA
        if fb < -1:
            if self._factor_balance(nodo.derecho) > 0:
                # CASO RL: enderezar el hijo derecho
                nodo.derecho = self._rotar_derecha(nodo.derecho)
            # CASO RR (o RL ya enderezado)
            return self._rotar_izquierda(nodo)

        return nodo        # ya estaba balanceado

    # ---------- búsqueda: SIN CAMBIOS respecto del BST ----------

    def contiene(self, clave):
        actual = self.raiz
        while actual is not None:
            if clave == actual.dato:
                return True
            actual = actual.izquierdo if clave < actual.dato else actual.derecho
        return False

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, acc):
        if nodo is None:
            return
        self._inorden(nodo.izquierdo, acc)
        acc.append(nodo.dato)
        self._inorden(nodo.derecho, acc)

    def altura(self):
        return self._altura(self.raiz)

    # ---------- eliminación: BST + rebalanceo ----------

    def eliminar(self, clave):
        if not self.contiene(clave):
            raise KeyError(clave)
        self.raiz = self._eliminar(self.raiz, clave)
        self._tamaño -= 1

    def _eliminar(self, nodo, clave):
        """Idéntico al del BST, con dos líneas al final:
        actualizar altura y rebalancear."""
        if nodo is None:
            return None

        if clave < nodo.dato:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, clave)
        elif clave > nodo.dato:
            nodo.derecho = self._eliminar(nodo.derecho, clave)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            sucesor = nodo.derecho
            while sucesor.izquierdo is not None:
                sucesor = sucesor.izquierdo
            nodo.dato = sucesor.dato
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.dato)

        # Las dos líneas que el BST no tenía:
        self._actualizar_altura(nodo)
        return self._rebalancear(nodo)

    # ---------- verificación del invariante ----------

    def es_avl_valido(self):
        """Verifica que TODO nodo cumple |fb| <= 1 y que las alturas
        almacenadas son correctas."""
        def verificar(nodo):
            if nodo is None:
                return True, -1
            ok_izq, h_izq = verificar(nodo.izquierdo)
            ok_der, h_der = verificar(nodo.derecho)
            altura_real = 1 + max(h_izq, h_der)
            ok = (ok_izq and ok_der
                  and abs(h_izq - h_der) <= 1
                  and nodo.altura == altura_real)
            return ok, altura_real

        return verificar(self.raiz)[0]
