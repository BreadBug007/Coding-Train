
angle = 0
wave = []

def setup():
    size(800, 600)

    
def draw():
    global angle, wave
    background(40)
    translate(200, 300)
    x, y = 0, 0
    
    for i in range(5):
        n = i + 1
        prevx, prevy = x, y
        radius = - 120 * 4 / ((-1^n) * n * PI)
        x += radius * cos(n * angle)
        y += radius * sin(n * angle)
        

        stroke(100, 200, 200)
        strokeWeight(2)
        noFill()
        circle(prevx, prevy, 2 * radius)
        line(prevx, prevy, x, y)

    wave.append(y)
    
    translate(300, 0)
    beginShape()
    for i in range(len(wave)):
        vertex(i, wave[::-1][i])   
    endShape()
    line(x - 300, y, 0, y)
    angle -= 0.05
    
    
