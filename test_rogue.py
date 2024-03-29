import numpy as np 
import pygame as pg 
from max import K



TAILLE_FENETRE = 800
TAILLE_CASE = 50
NB_CASES = TAILLE_FENETRE // TAILLE_CASE

FPS=30

class Hero:
    def __init__(self, health, attack, x, y, color, direction):
        self.health = health
        self.attack = attack
        self.x = x
        self.y = y
        self.i=y
        self.j=x
        self.alive = True
        self.color = color
        self.direction = direction

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x*TAILLE_CASE,self.y*TAILLE_CASE,TAILLE_CASE,TAILLE_CASE))

    def update_health(self):
        if self.health <= 0:
            self.alive = False

    def attack_enemy(self, enemy):
        damage = np.random.randint(self.attack - 5, self.attack + 5)
        enemy.health -= damage
        enemy.is_dead()

class Jeton:

    def __init__(self, color):
        self.y = 0
        self.color = color
        self.x = 0

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x*TAILLE_CASE,self.y*TAILLE_CASE), 6)

    def update_position(self):
        self.y += 5

def display(screen,board):
    pg.display.set_caption('Rogue')
    screen.fill((255,255,255))
    for i in range(NB_CASES):
        for j in range(NB_CASES):
            #on colorie en noir les bordures
            if board[i][j]==1:
                pg.draw.rect(screen,(0,0,0),(j*TAILLE_CASE,i*TAILLE_CASE,TAILLE_CASE,TAILLE_CASE))
            if board[i][j]==2:
                pg.draw.rect(screen,(0,0,255),(j*TAILLE_CASE,i*TAILLE_CASE,TAILLE_CASE,TAILLE_CASE))
                ##on colorie en bleu les portes


def main():
    ex_board=np.zeros((NB_CASES,NB_CASES))
    #on veut faire deux salles , c'est à dire des carrées remplies de 1 en haut à gauche et en bas à droite de dimension nb case/2
    ex_board[1:NB_CASES//2-1,1:NB_CASES//2-1]=np.ones((NB_CASES//2-2,NB_CASES//2-2))
    ex_board[1,7]=2
    ex_board[NB_CASES//2+1:NB_CASES-1,NB_CASES//2+1:NB_CASES-1]=np.ones((NB_CASES//2-2,NB_CASES//2-2))
    ex_board[14,8]=2

    dic_porte={(1,7):[14,9],(14,8):[1, 6]}
   
    print(ex_board[1,7], ex_board[14,8])
    print(ex_board)
    pg.init()

    pg.font.init()
    police = pg.font.Font(None, 36)  # Choisissez une taille de police qui convient

    screen = pg.display.set_mode((TAILLE_FENETRE,TAILLE_FENETRE))

    monstre = K(14, 14, [0,0])
    monstre.display(screen, TAILLE_CASE)


    pg.display.set_caption('Rogue')
    clock=pg.time.Clock()
    running=True
    #la boucle principale
    jetons = []
    score = 0

    hero = Hero(100, 10, 3, 3, (255, 0, 0), [0, 0])


    while running:
        
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        display(screen,ex_board)

        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
            #la touche q doit arrêter le jeu
            if event.type==pg.KEYDOWN:
                hero.draw(screen)
                if event.key==pg.K_q:
                    running=False
                elif event.key == pg.K_DOWN:
                    if ex_board[hero.y+1,hero.x]==1:
                        hero.y += 1
                        #monstre.se_deplacer(hero.x, hero.y)
                        #hero.direction = [-1, 0]
                    if ex_board[hero.y+1,hero.x]==2:
                        print("ok")
                        if (hero.y+1, hero.x) in dic_porte:
                            a,b=hero.y+1,hero.x
                            hero.y = dic_porte[(a,b)][0]
                            hero.x = dic_porte[(a,b)][1]
                            #monstre.se_deplacer(hero.x, hero.y)
                            hero.direction = [-1, 0]
                elif event.key == pg.K_UP:
                    if ex_board[hero.y-1,hero.x]==1:
                        hero.y -= 1
                        #monstre.se_deplacer(hero.x, hero.y)
                        #hero.direction = [1, 0]
                    if (hero.y-1,hero.x) in dic_porte:
                        a,b=hero.y-1,hero.x
                        hero.y = dic_porte[(a,b)][0]
                        hero.x = dic_porte[(a,b)][1]
                        #monstre.se_deplacer(hero.x, hero.y)
                        hero.direction = [1, 0]
                elif event.key == pg.K_LEFT:
                    print(dic_porte, hero.x, hero.y)
                    if ex_board[hero.y,hero.x-1]==1:
                        hero.x -= 1
                        #monstre.se_deplacer(hero.x, hero.y)
                        hero.direction = [0, -1]
                    if (hero.y,hero.x-1) in dic_porte.keys():
                        a,b=hero.y,hero.x-1
                        hero.y = dic_porte[(a,b)][0]
                        hero.x = dic_porte[(a,b)][1]
                        #monstre.se_deplacer(hero.x, hero.y)
                        hero.direction = [0, -1]
                elif event.key == pg.K_RIGHT:
                    if ex_board[hero.y,hero.x+1]==1:
                        hero.x += 1
                        #monstre.se_deplacer(hero.x, hero.y)
                        hero.direction = [0, 1]
                        print((hero.y,hero.x)==(1,6),"yeah",dic_porte.keys())
                    if ex_board[hero.y,hero.x+1]==2:
                        if (hero.y,hero.x+1 ) in dic_porte.keys():
                            a,b=hero.y,hero.x+1 
                            hero.y = dic_porte[(a,b)][0]
                            print(hero.y,hero.x)
                            hero.x = dic_porte[(a,b)][1]
                            print(hero.y,hero.x)
                        #monstre.se_deplacer(hero.x, hero.y)
                        hero.direction = [0, 1]


        
        """
        if monstre.attaque(hero.x, hero.y):
            hero.health -= 10
            # on fait reculer le héro et le monstre après collision
            if hero.direction[0] != 0 :
                hero.x -= hero.direction[0]
                n=1
                while ex_board[hero.x - hero.direction[0]][hero.y] == 0 and n<4 : 
                    hero.x -= hero.direction[0]
                    n+=1
            else : 
                hero.y = hero.y - hero.direction[1]
                n=1
                while ex_board[hero.x][hero.y - hero.direction[1]] == 0 and n<4 : 
                    hero.y -= hero.direction[1]
                    n+=1

            if monstre.direction[0] != 0 :
                monstre.x = monstre.x - monstre.direction[0]
                n=1
                while ex_board[monstre.x - monstre.direction[0]][hero.y] == 0 and n<4 : 
                    monstre.x -= monstre.direction[0]
                    n+=1
            else : 
                monstre.y -= monstre.direction[1]
                n=1
                while ex_board[monstre.x][monstre.y - monstre.direction[1]] == 0 and n<4 : 
                    monstre.y -= monstre.direction[1]   
                    n+=1     
            """
            
        
        screen.fill((0, 0, 0))
        display(screen,ex_board)
        
                
        
        

        
        screen.fill((0, 0, 0))
        display(screen,ex_board)        
        monstre.display(screen, TAILLE_CASE)

        hero.draw(screen)
        
        for jeton in jetons:
            jeton.draw(screen)
            if jeton.x == hero.x and abs(jeton.y - hero.y) < 26:
                jetons.remove(jeton)
                score += 1 

        texte_score = police.render("Score : " + str(hero.health), True, (125, 125, 125))
        position_score = (10, 10) 
        screen.blit(texte_score, position_score)
        hero.update_health()
        pg.display.update()
        if not hero.alive:
            running = False
            pg.quit()
        
        
    pg.quit()

if __name__ == "__main__":
    main()
