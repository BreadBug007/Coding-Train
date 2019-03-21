class Pendulum():
    
    def __init__(self):
        
        self.x = 0          # x position
        self.y = 0          # y position
        self.r = 0          # length
        self.m = 0          # mass
        self.a = PI/2       # angle
        self.v =  0         # velocity
        self.acc = 0        # acceleration
        
    def update(self):
        
        self.v += self.acc
        self.a += self.v
