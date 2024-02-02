import random
import pygame as pg

class K():
    def __init__(self, x, y):
        self.x = -2
        self.y = -2
    

    def __repr__(self):
        return str(self.x, self.y)
    
    def se_deplacer(self, X, Y):   
        # le monstre se déplace vers le personnage
        if round(((X - self.x)/self.distance(X, Y))) == round(((Y - self.y)/self.distance(X, Y))) :
            #on étudie les cas où le monstre et le personnage sont un peu en diagonale, il ne faut alors pas que le monstre se déplace en diagonale
            if ((X - self.x)/self.distance(X, Y)) < ((Y - self.y)/self.distance(X, Y)):
                if self.y < Y:
                    self.y = self.y + 1 
                
                else:   
                    self.y = self.y - 1

            elif ((X - self.x)/self.distance(X, Y)) > ((Y - self.y)/self.distance(X, Y)):
                if self.x < X:
                    self.x = self.x + 1
                else:
                    self.x = self.x - 1 

            else :
                a = random.randint(0,1)
                if a == 1 : 
                    if self.x < X : 
                        self.x = self.x + 1 
                    else : 
                        self.x = self.x - 1
                else :
                    if self.y < Y : 
                        self.y = self.y + 1 
                    else : 
                        self.y = self.y - 1 

                
                

                

        
        else:
            self.x += round(((X - self.x)/self.distance(X, Y)))
            self.y += round(((Y - self.y)/self.distance(X, Y)))

        return self.x, self.y
    

    def attaque(self, X, Y):   #si le monstre est proche du personnage, il l'attaque
        if self.distance(X, Y) <= 1:
            return True
        else:
            return False


    def distance(self, X, Y):
        return ((X - self.x)**2 + (Y - self.y)**2)**0.5
    
    
    def display(self):
        pg.draw.circle(screen, (0, 0, 255), (self.x, self.y), 15)







    
    



  

