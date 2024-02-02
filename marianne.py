import numpy as np 
import pygame as pg

class P() :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def guerison(self, X, Y):   #si le monstre est proche du personnage, il l'attaque

        if self.distance(X, Y) == 0:

            return True
        else:
            return False


    def display(self,screen, TAILLE_CASE):
        pg.draw.circle(screen, (0, 255, 0), ((self.x+0.5)*TAILLE_CASE, (self.y+0.5)*TAILLE_CASE), 15)
