# El nodo Z está desbalanceado. Mira el signo de fb(Z) y el del hijo.
#
# ┌──────────┬───────────────┬────────┬──────────────────────────┐
# │  fb(Z)   │  fb(hijo)     │  Caso  │  Solución                │
# ├──────────┼───────────────┼────────┼──────────────────────────┤
# │  > +1    │  >= 0         │   LL   │  rotar_derecha(Z)        │
# │  > +1    │  <  0         │   LR   │  rotar_izquierda(Z.izq)  │
# │          │               │        │  luego rotar_derecha(Z)  │
# │  < -1    │  <= 0         │   RR   │  rotar_izquierda(Z)      │
# │  < -1    │  >  0         │   RL   │  rotar_derecha(Z.der)    │
# │          │               │        │  luego rotar_izquierda(Z)│
# └──────────┴───────────────┴────────┴──────────────────────────┘
#
# CASO LL — inserción en el izquierdo del izquierdo
#        Z(fb=+2)              Y
#       /                    /   \
#      Y(fb=+1)     =>      X     Z
#     /
#    X
#
# CASO RR — inserción en el derecho del derecho (espejo de LL)
#     Z(fb=-2)                  Y
#       \                     /   \
#        Y(fb=-1)     =>     Z     X
#          \
#           X
#
# CASO LR — inserción en el DERECHO del izquierdo
#      Z(fb=+2)          Z(fb=+2)             X
#     /                 /                   /   \
#    Y(fb=-1)   =>     X          =>       Y     Z
#     \               /
#      X             Y
#   (1) rotar_izquierda(Y)      (2) rotar_derecha(Z)
#
# CASO RL — espejo de LR
#   (1) rotar_derecha(hijo derecho)   (2) rotar_izquierda(Z)
#
# TRUCO PARA RECORDAR:
#   Si el desbalance va en LÍNEA RECTA (LL o RR) -> UNA rotación
#   Si va en ZIGZAG (LR o RL)                    -> DOS rotaciones
#                                                   (endereza, luego rota)