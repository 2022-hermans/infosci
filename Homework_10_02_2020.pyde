
def setup():
    background(255)
    size(1000,1000)
    textAlign(CENTER,CENTER)
    
def draw():
    print(" ")
    
def mouseClicked():
    x = mouseX
    y = mouseY
    f = random(10,80)
    myred = random(0,255)
    mygreen = random(0,255)
    myblue = random(0,255)
    fill(myred, mygreen, myblue)
    circle(x,y,f)
    fill(0)
    textSize(f)
    text("Chihoo",x,y)
    line(x , y ,500 ,500)
    
    print (x,y)
