def setup():
    size(600, 600)

def draw():
    translate(width/2,height/2)
    beginShape()
    for i in range(6):
        vertex(100,100)
        rotate(radians(60))
    endShape(CLOSE)
