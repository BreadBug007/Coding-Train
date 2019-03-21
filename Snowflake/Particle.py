class Snowflake:
    
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.r = 4
        
    def update(self):
        self.pos.x -= 1
        self.pos.y += random(-3, 3)
        angle = self.pos.heading()
        magnitude = self.pos.mag()
        angle = constrain(angle, 0, PI/6)
        self.pos = PVector.fromAngle(angle)
        self.pos.setMag(magnitude)
        
    def finished(self):
        return self.pos.x <= 1
    
    def intersect(self, other):
        for s in other:
            d = dist(self.pos.x, self.pos.y, s.pos.x, s.pos.y)
            if d < self.r:
                return True
    
    def show(self):
        fill(100, 200, 255, 150)
        stroke(200, 100)
        circle(self.pos.x, self.pos.y, self.r)
