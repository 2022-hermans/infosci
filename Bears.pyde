x = 0


        
def draw():
    global x
    background(255)
    strokeWeight(2)
    
    if x==1:
        print(x),("bear")
    else:
        print(x),("bears")
    
    x = x + 1
    if x == 101:
        sys.exit()
    


    delay(100)
