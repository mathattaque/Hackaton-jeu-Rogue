import numpy as np 
import pygame as pg 


TAILLE_FENETRE = 800
TAILLE_CASE = 50
NB_CASES = TAILLE_FENETRE // TAILLE_CASE

FPS=30


class Hero:
    def __init__(self, name, health, attack, x, y, color):
        self.name = name
        self.health = health
        self.attack = attack
        self.x = x
        self.y = y
        self.alive = True
        self.color = color

    def draw(self, screen):
        ellipse_rect = pg.Rect(self.x - TAILLE_CASE, self.y + TAILLE_CASE, 50, 30)
        pg.draw.ellipse(screen, self.color, ellipse_rect)

    def is_dead(self):
        if self.health <= 0:
            self.alive = False

    def attack_enemy(self, enemy):
        damage = np.random.randint(self.attack - 5, self.attack + 5)
        enemy.health -= damage
        enemy.is_dead()




def display(screen,board):
    pg.display.set_caption('Rogue')
    screen.fill((255,255,255))
    for i in range(NB_CASES):
        for j in range(NB_CASES):
            #on colorie en noir les bordures
            if board[i][j]==1:
                pg.draw.rect(screen,(0,0,0),(i*TAILLE_CASE,j*TAILLE_CASE,TAILLE_CASE,TAILLE_CASE))

    


def main():

    #pour l'exemple
    ex_board=np.zeros((NB_CASES,NB_CASES))
    ex_board[1:NB_CASES-1,1:NB_CASES-1]=np.ones((NB_CASES-2,NB_CASES-2))
    #print(ex_board)

        
    pg.init()
    screen = pg.display.set_mode((TAILLE_FENETRE,TAILLE_FENETRE))
    pg.display.set_caption('Rogue')
    clock=pygame.time.Clock()
    running=True
    #la boucle principale
    while running:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
            #la touche q doit arrêter le jeu
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_q:
                    running=False
        display(screen,ex_board)

        pg.display.update()
        clock.tick(FPS)
    texte_score = police.render("Score : " + str(score), True, (255, 255, 255))
    position_score = (10, 10) 
    screen.blit(texte_score, position_score)

if __name__ == "__main__":
    main()