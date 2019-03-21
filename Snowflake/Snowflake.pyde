from Particle import Snowflake

snow = []

def setup():
    global current
    size(600, 600)
    current = Snowflake(width/2, 0)
    
    
    
def draw():
    global current
    
    translate(width/2, height/2)
    background(0)
    rotate(PI/6)

    
    while not current.finished() and not current.intersect(snow):
        current.update()

    snow.append(current)
    current = Snowflake(width/2, 0)

    for i in range(6):
        rotate(PI/3)
        current.show()
        for particle in snow:
            particle.show()
    
        pushMatrix()
        scale(1, -1)
        current.show()
        for particle in snow:
            particle.show()
        popMatrix()
    save("Snowflake.jpg")
