import numpy as np 

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
        ellipse_rect = pg.Rect(self.x - TAILLE.CASE, self.y + TAILLE.CASE, 50, 30)
        pg.draw.ellipse(screen, self.color, ellipse_rect)

    def is_dead(self):
        if self.health <= 0:
            self.alive = False

    def attack_enemy(self, enemy):
        damage = np.random.randint(self.attack - 5, self.attack + 5)
        enemy.health -= damage
        enemy.is_dead()



texte_score = police.render("Score : " + str(score), True, (255, 255, 255))
position_score = (10, 10) 
screen.blit(texte_score, position_score)

def main():
    pass