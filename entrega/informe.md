# Informe: BST frente a AVL en matrículas académicas

## Objetivo

Comprobar qué ocurre al insertar documentos en orden ascendente en un árbol binario de búsqueda (BST) y comparar el resultado con un árbol AVL. Se mide altura y tiempo de búsqueda con 10.000 claves.

## Entorno y método

- Python 3, `time.perf_counter()`.
- N = 10.000 documentos (`1` a `10.000`).
- 1.000 búsquedas por escenario, con las mismas claves de consulta.
- Semilla aleatoria: `2026`, para poder repetir la permutación.
- La altura se mide en aristas: árbol vacío = -1; hoja = 0.
- Los tiempos son una ejecución de referencia del entorno donde se preparó esta entrega. Pueden variar según el equipo; las alturas y el número de rotaciones son reproducibles.

Ejecutar desde esta carpeta:

```bash
python benchmark.py
pytest -v
```

## Parte A y C: resultados

| Escenario | Altura (aristas) | Inserción (ms) | 1.000 búsquedas (ms) | Rotaciones |
|---|---:|---:|---:|---:|
| BST ordenado | 9.999 | 2.212,644 | 236,009 | 0 |
| BST desordenado | 28 | 61,965 | 0,955 | 0 |
| AVL ordenado | 13 | 44,387 | 0,875 | 9.986 |
| AVL desordenado | 15 | 45,304 | 0,654 | 6.948 |

**Interpretación:** el BST ordenado se convierte en una cadena de 10.000 nodos. Una búsqueda puede recorrer casi todos ellos; la altura es `n - 1` y las operaciones pueden costar O(n). El BST con entrada desordenada sale mucho mejor en esta ejecución, pero su balance depende del orden de llegada y no tiene garantía de peor caso. El AVL conserva altura pequeña en ambos órdenes y garantiza O(log n) para búsqueda, inserción y eliminación.

El número de rotaciones contabiliza cada rotación simple. Una rotación doble (LR o RL) cuenta como dos rotaciones simples. En AVL, insertar claves estrictamente crecientes provoca una rotación a medida que se corrige cada desbalance; por eso se registran 9.986 rotaciones para 10.000 claves. Las rotaciones son trabajo extra, pero evitan que las búsquedas se degraden.

## Parte B: por qué degenera el BST

El BST compara cada clave con la raíz y continúa a la izquierda o a la derecha. Si se insertan claves crecientes `1, 2, 3, ...`, cada nueva clave es mayor que todas las anteriores y se coloca como hijo derecho del último nodo. No aparece ninguna rama izquierda.

Árbol con los primeros siete documentos ordenados:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
           \
            7
```

Esto se parece a una **lista enlazada** (una cadena), no a un árbol equilibrado. Para buscar `7`, hay que visitar los siete nodos; con 10.000 documentos, una búsqueda al final puede visitar los 10.000. La implementación puede ser correcta y aun así tener un rendimiento pésimo: el problema es la forma de los datos y la falta de balance.

## Parte C: solución AVL y rotaciones

El AVL es un BST que mantiene en cada nodo:

`factor_balance = altura(izquierdo) - altura(derecho)`

Para todo nodo debe cumplirse `-1 <= factor_balance <= 1`. Las alturas se guardan en los nodos y se actualizan al volver por el camino de inserción o eliminación. Si aparece un desbalance, se aplica el caso correspondiente:

- **LL:** rotación simple a la derecha.
- **RR:** rotación simple a la izquierda.
- **LR:** rotación a la izquierda del hijo izquierdo y luego a la derecha del nodo desbalanceado.
- **RL:** rotación a la derecha del hijo derecho y luego a la izquierda del nodo desbalanceado.

Las pruebas verifican los cuatro casos, el orden inorden, la altura guardada y el invariante AVL incluso después de eliminar nodos.

## Parte D: respuesta al jefe de sistemas

**Desordenar el archivo no es una solución robusta.** Puede mejorar la forma inicial del BST, como muestran los 10.000 datos desordenados (altura 28 frente a 9.999), pero solo cambia la probabilidad del problema: no ofrece una garantía. Si los documentos extemporáneos llegan en orden creciente (o el patrón de inserción produce una rama larga), el BST puede volver a degenerar. Además, la carga inicial se repite cada semestre y no conviene depender de cómo venga aleatorizado el archivo.

Un AVL mantiene el balance tras **cada** inserción y eliminación, tanto durante la carga inicial como durante el semestre. En la prueba ordenada, la altura fue 13 para 10.000 claves, frente a 9.999 en el BST. Por eso la recomendación es utilizar AVL (o una estructura balanceada equivalente) si el requisito es rendimiento predecible, y no depender de barajar el archivo.

## Archivos entregados

- `bst.py`: inserción, búsqueda, altura, recorrido inorden, validación y eliminación de hoja, nodo con un hijo y nodo con dos hijos.
- `test_bst.py`: pruebas de los casos de eliminación, incluida la validación del BST tras borrar un nodo con dos hijos.
- `avl.py`: cuatro rotaciones, actualización de alturas, rebalanceo al insertar y eliminar, y contador de rotaciones simples.
- `test_avl.py`: pruebas de rotaciones y de invariantes AVL.
- `benchmark.py`: experimento reproducible para los cuatro escenarios.
