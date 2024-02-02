class K():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    
    def __repr__(self):
        return str(self.x)
    
    def se_deplacer(self, X, Y):   
        # le monstre se déplace vers le personnage
        if round(((X - self.x)/self.distance(X, Y))) == round(((Y - self.y)/self.distance(X, Y))) :
            if ((X - self.x)/self.distance(X, Y)) < ((Y - self.y)/self.distance(X, Y)):
                if self.y < Y:
                    self.y = self.y + 1 
                    self.direction = [0, 1]
                else:   
                    self.y = self.y - 1
                    self.direction = [0, -1]
            else:
                if self.x < X:
                    self.x = self.x + 1
                    self.direction = [1, 0]
                else:
                    self.x = self.x - 1 
                    self.direction = [-1, 0]
    

        
        else:
            self.x = self.x + round(((X - self.x)/self.distance(X, Y)))
            self.y = self.y + round(((Y - self.y)/self.distance(X, Y)))

        return self.x, self.y
    
    def attaque(self, X, Y):
        if self.distance(X, Y) == 1:
            return True
        else:
            return False


    def distance(self, X, Y):
        return ((X - self.x)**2 + (Y - self.y)**2)**0.5
    
    



  

