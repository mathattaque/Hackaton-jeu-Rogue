import random
import pygame as pg







class K():

    def __init__(self, x, y, direction, salle):
        self.x = x 
        self.y = y
        self.salle = salle
        #self.etat = "inactive"
        self.etat = "active"
    

    def activate(self, salle):
        if salle.etat == "ouverte":
            self.etat = "active"

    def __repr__(self):
        return str(self.x, self.y)
    
    def se_deplacer(self, X, Y):   
        # le monstre se déplace vers le personnage  
        if self.etat == "active":

            if self.distance(X, Y) != 0:
                if round(((X - self.x)/self.distance(X, Y))) == round(((Y - self.y)/self.distance(X, Y))) :
                    #on étudie les cas où le monstre et le personnage sont un peu en diagonale, il ne faut alors pas que le monstre se déplace en diagonale
                    if ((X - self.x)/self.distance(X, Y)) < ((Y - self.y)/self.distance(X, Y)):
                        if self.y < Y:
                            self.y += 1 
                            self.direction = [0, 1]
                        
                        else:   
                            self.y -= 1
                            self.direction = [0, -1]


                    elif ((X - self.x)/self.distance(X, Y)) > ((Y - self.y)/self.distance(X, Y)):
                        if self.x < X:
                            self.x += 1
                            self.direction = [1, 0]
                        else:
                            self.x -= 1 
                            self.direction = [-1, 0]

                    else :
                        a = random.randint(0,1)
                        if a == 1 : 
                            if self.x < X : 
                                self.x += 1 
                                self.direction = [1, 0]
                            else : 
                                self.x -= 1
                                self.direction = [-1, 0]
                        else :
                            if self.y < Y : 
                                self.y += 1 
                                self.direction = [0, 1]
                            else : 
                                self.y -= 1
                                self.direction = [0, -1]

                else:
                    
                    self.x += round(((X - self.x)/self.distance(X, Y))) if self.distance(X, Y) != 0 else 0
                    self.y += round(((Y - self.y)/self.distance(X, Y))) if self.distance(X, Y) != 0 else 0
            else:
                self.x, self.y = self.x, self.y
        

        return self.x, self.y
    

    def attaque(self, X, Y):   #si le monstre est proche du personnage, il l'attaque
        if self.etat == "active":
            if self.distance(X, Y) <= 1:
                return True
            else:
                return False
        

    def distance(self, X, Y):
        return ((X - self.x)**2 + (Y - self.y)**2)**0.5
    

    def display(self,screen, TAILLE_CASE):
        pg.draw.circle(screen, (0, 0, 255), ((self.x + 1/2)*TAILLE_CASE , (self.y + 1/2)*TAILLE_CASE), 15)





class salle():
    def __init__(self, i, j, dico, width, height):
        self.i = i
        self.j = j
        self.width = width
        self.height = height
        self.entrees = dico
        #self.etat = "fermee"
        self.etat = "ouverte"


    def draw(self, board):
        board[self.i:self.i+self.width, self.j:self.j+self.height] = 1
        return board
    
    
    def activate(self, entrees, hero):
        if (hero.x, hero.y) in entrees:
            if self.etat ==  "ouverte":
                self.etat = "fermee"
            else:
                self.etat = "ouverte"
    

            
    





    
    



  

