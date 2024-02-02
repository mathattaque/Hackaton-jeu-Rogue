import numpy as np
TAILLE_FENETRE = 800
TAILLE_CASE = 50
NB_CASES = TAILLE_FENETRE // TAILLE_CASE

ex2_board=np.zeros((NB_CASES,NB_CASES))
#on veut faire deux salles , c'est à dire des carrées remplies de 1 en haut à gauche et en bas à droite de dimension nb case/2
ex2_board[1:NB_CASES//2-1,1:NB_CASES//2-1]=np.ones((NB_CASES//2-2,NB_CASES//2-2))
ex2_board[6,7]=2
ex2_board[NB_CASES//2+1:NB_CASES-1,NB_CASES//2+1:NB_CASES-1]=np.ones((NB_CASES//2-2,NB_CASES//2-2))
ex2_board[8,11]=2

dic_porte={(6,7):(8,11),(8,11):(6,7)}
print(ex2_board)
