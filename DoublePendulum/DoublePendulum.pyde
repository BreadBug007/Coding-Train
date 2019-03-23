from Pendulum import Pendulum

p1 = Pendulum()
p2 = Pendulum()

g = 1
p1.r = 100
p2.r = 100
p1.m = 10
p2.m = 10
x2, y2 = 0, 0


def setup():
    global canvas
    
    size(1200, 800, P2D)
    canvas = createGraphics(width, height)
    canvas.beginDraw() 
    canvas.background(200)
    canvas.endDraw()   
    
def draw():
    
    global g, x2, y2
    image(canvas,0,0)
    translate(width/2, 300)
    
    
    num1 = -g*(2*p1.m + p2.m)*sin(p1.a) - p2.m*g*sin(p1.a - 2*p2.a)
    num2 = -2*sin(p1.a - p2.a)*p2.m
    num3 = p2.v*p2.v*p2.r + p1.v*p1.v*p1.r*cos(p1.a - p2.a)
    den = p1.r*(2*p1.m+p2.m - p2.m*cos(2*p1.a - 2*p2.a))
    
    p1.acc = (num1 + num2*num3)/den
    
    num1 = 2*sin(p1.a - p2.a)
    num2 = (p1.v*p1.v*(p1.m + p2.m))
    num3 = g*(p1.m + p2.m)*cos(p1.a)
    num4 = p2.v*p2.v*p1.r*p2.m*cos(p1.a - p2.a)
    den = p2.r*(2*p1.m+p2.m - p2.m*cos(2*p1.a - 2*p2.a))

    p2.acc = (num1 * (num2 + num3 + num4))/den
    
    
    p1.update()
    p2.update()
    
    p1.x = p1.r * sin(p1.a)
    p1.y = p1.r * cos(p1.a)


    line(0, 0, p1.x, p1.y)
    fill(50, 50, 50)
    circle(p1.x, p1.y, 20)
    
    p2.x = p1.x + p2.r * sin(p2.a)
    p2.y = p1.y + p2.r * cos(p2.a)

    line(p1.x, p1.y, p2.x, p2.y)
    fill(50, 50, 50)
    circle(p2.x, p2.y, 20)

    
    
    canvas.beginDraw() 
    canvas.translate(width/2, 300)
    canvas.strokeWeight(2)
    canvas.stroke(200, 100, 50)
    if frameCount >1:
        canvas.line(x2, y2, p2.x, p2.y)
    canvas.endDraw() 
    
    x2, y2 = p2.x, p2.y
