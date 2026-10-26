# factor_balance(n) = altura(n.izquierdo) - altura(n.derecho)
#
# Un árbol es AVL si TODO nodo tiene factor de balance en {-1, 0, +1}.
#
# Recuerda: altura(None) = -1
#
# ÁRBOL 1:                ÁRBOL 2:
#       50                    50
#      /  \                  /
#    30    70               30
#                          /
#                        20
#
#   fb(30) = -1-(-1)= 0             fb(20) = -1-(-1)=0
#   fb(70) = -1-(-1)=0            fb(30) = 0-(-1)=0
#   fb(50) = 0-0=0            fb(50) = 1-(-1)=2
#   ¿Es AVL?   si es AVL             ¿Es AVL? no es AVl ¿Qué nodo está desbalanceado?  el 50 su factor es 2
#
# ÁRBOL 3:                ÁRBOL 4:
#       50                    50
#      /                     /
#    30                    30
#      \                     \
#       40                     40
#                                \
#                                 45
#
#   ¿Cuál nodo se desbalancea primero al insertar?
#    en el 3, es el 50 que con factor 2 y en el 4 es el 30 queda con factor -2
#   ¿Es el mismo tipo de desbalance en los dos casos?
#   no el 3 es como un zig zag en cambio el 4 es lineal