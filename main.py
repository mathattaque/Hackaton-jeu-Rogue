import numpy as np 
import pygame as pg 
from max import K



TAILLE_FENETRE = 800
TAILLE_CASE = 50
NB_CASES = TAILLE_FENETRE // TAILLE_CASE

FPS=30

class Hero:
    def __init__(self, health, attack, x, y, color):
        self.health = health
        self.attack = attack
        self.x = x
        self.y = y
        self.alive = True
        self.color = color

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x*TAILLE_CASE,self.y*TAILLE_CASE,TAILLE_CASE,TAILLE_CASE))

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

    pg.font.init()
    police = pg.font.Font(None, 36)  # Choisissez une taille de police qui convient

    screen = pg.display.set_mode((TAILLE_FENETRE,TAILLE_FENETRE))

    monstre = K()
    monstre.display()

    pg.display.set_caption('Rogue')
    clock=pg.time.Clock()
    running=True
    #la boucle principale

    score = 0


    hero = Hero(100, 10, 400, 400, (255, 0, 0))

    while running:
        clock.tick(FPS)

    hero = Hero(100, 10, 8, 8, (255, 0, 0))

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        display(screen,ex_board)


        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
            #la touche q doit arrêter le jeu
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_q:
                    running=False

        
        monstre.se_deplacer(hero.x, hero.y)
        if monstre.attaque(hero.x, hero.y):
            hero.health -= 100

        
        screen.fill((0, 0, 0))
        display(screen,ex_board)

                elif event.key == pg.K_LEFT:
                    if ex_board[hero.x-1,hero.y]==1:
                        hero.x -= 1
                elif event.key == pg.K_RIGHT:
                    if ex_board[hero.x+1,hero.y]==1:
                        hero.x += 1
                elif event.key == pg.K_UP:
                    if ex_board[hero.x,hero.y-1]==1:
                        hero.y -= 1
                elif event.key == pg.K_DOWN:
                    if ex_board[hero.x,hero.y+1]==1:
                        hero.y += 1

        if not hero.alive():
            pg.quit()

        hero.draw(screen)
        
        texte_score = police.render("Score : " + str(score), True, (125, 125, 125))
        position_score = (10, 10) 
        screen.blit(texte_score, position_score)

        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()