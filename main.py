def main():
<<<<<<< Updated upstream
    pass
=======

    #pour l'exemple
    ex_board=np.zeros((NB_CASES,NB_CASES))
    ex_board[1:NB_CASES-1,1:NB_CASES-1]=np.ones((NB_CASES-2,NB_CASES-2))
    #print(ex_board)
    pg.init()

    pg.font.init()
    police = pg.font.Font(None, 36)  # Choisissez une taille de police qui convient

    screen = pg.display.set_mode((TAILLE_FENETRE,TAILLE_FENETRE))

    monstre = K(14, 14, [0,0])
    monstre.display(screen, TAILLE_CASE)

    potion = P(1,1)
    potion.display(screen, TAILLE_CASE)


    pg.display.set_caption('Rogue')
    clock=pg.time.Clock()
    running=True
    #la boucle principale
    jetons = []
    score = 0



    hero = Hero(100, 10, 8, 8, (255, 0, 0), [0, 0])


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
                elif event.key == pg.K_LEFT:
                    if ex_board[hero.x-1,hero.y]==1:
                        hero.x -= 1
                        monstre.se_deplacer(hero.x, hero.y)
                        hero.direction = [-1, 0]
                elif event.key == pg.K_RIGHT:
                    if ex_board[hero.x+1,hero.y]==1:
                        hero.x += 1
                        monstre.se_deplacer(hero.x, hero.y)
                        hero.direction = [1, 0]
                elif event.key == pg.K_UP:
                    if ex_board[hero.x,hero.y-1]==1:
                        hero.y -= 1
                        monstre.se_deplacer(hero.x, hero.y)
                        hero.direction = [0, -1]
                elif event.key == pg.K_DOWN:
                    if ex_board[hero.x,hero.y+1]==1:
                        hero.y += 1
                        monstre.se_deplacer(hero.x, hero.y)
                        hero.direction = [0, 1]


        
        
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


            if potion.guerison
            
            
        
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
>>>>>>> Stashed changes
