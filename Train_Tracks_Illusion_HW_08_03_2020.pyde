offset = 440
change = 45

def mouseClicked():
    global offset
    global change
    if (offset < 40):
        change = -45
        
    if (offset > 460):
        change = 45
    offset = offset - change

def setup():
    size(500,500)
  
def draw():
    background(255) #rgb
    fill(0)
    stroke(0)
    strokeWeight(3)
    line(200,0,50,500)
    line(300,0,450,500)
    strokeWeight(10)
    line(10,460,490,460)
    line(65,310,435,310)
    line(115,195,385,195)
    line(150,110,350,110)
    line(170,55,330,55)
    line(185,20,315,20)
    stroke(255,0,0)
    if (offset == 35):
        stroke(255,255,0)
    line(185,35,315,35)
    stroke(0,255,0)
    global offset
    
    if (offset == 35):
        stroke(255,255,0)
    line(185,offset,315,offset)
