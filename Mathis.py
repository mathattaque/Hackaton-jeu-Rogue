import pygame as pg
import numpy as np



class Hero:
    def __init__(self, health, attack, x, y, color, direction):
        self.health = health
        self.attack = attack
        self.x = x
        self.y = y
        self.alive = True
        self.color = color
        self.direction = direction

    def draw(self, screen, TAILLE_CASE):
        pg.draw.rect(screen, self.color, (self.x*TAILLE_CASE, self.y*TAILLE_CASE ,TAILLE_CASE, TAILLE_CASE))

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

    def draw(self, screen, TAILLE_CASE):
        pg.draw.circle(screen, self.color, (self.x*TAILLE_CASE,self.y*TAILLE_CASE), 6)

    def update_position(self):
        self.y += 5
