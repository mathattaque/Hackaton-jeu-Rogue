import pygame
import numpy as np


TAILLE_FENETRE = 800
TAILLE_CASE = 50
NB_CASES = TAILLE_FENETRE // TAILLE_CASE


def display(screen,board):
    pygame.display.set_caption('Rogue')
    screen.fill((255,255,255))
    for i in range(NB_CASES):
        for j in range(NB_CASES):
            #on colorie en noir les bordures
            if board[i][j]==1:
                pygame.draw.rect(screen,(0,0,0),(i*TAILLE_CASE,j*TAILLE_CASE,TAILLE_CASE,TAILLE_CASE))
    





def main():

    #pour l'exemple
    ex_board=np.zeros((NB_CASES,NB_CASES))
    ex_board[1:NB_CASES-1,1:NB_CASES-1]=np.ones((NB_CASES-2,NB_CASES-2))
    #print(ex_board)


    #initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((TAILLE_FENETRE,TAILLE_FENETRE))
    pygame.display.set_caption('Rogue')
    running=True
    #la boucle principale
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            #la touche q doit arrêter le jeu
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    running=False
        display(screen,ex_board)

        pygame.display.update()


if __name__ == "__main__":
    main()