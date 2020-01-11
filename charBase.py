class charBase:
    name  = ""
    maxlife = 100
    currentLife = 0
    dead = False
    def __init__(self, name, maxlife):
        self.name = name
        self.maxlife = maxlife
        self.currentLife = maxlife
        
    def applyCure(self,cureValue):
        self.currentLife += cureValue
        if self.currentLife > self.maxlife:
            self.currentLife = self.maxlife
            
    def applyDamage(self,damageValue):
        if self.currentLife > 0:
            self.currentLife -= damageValue
        else:
            self.dead = True
            
        
        
    
     