x = 1900



        
def draw():
    global x
    background(255)
    strokeWeight(2)
    print("the year is"),(x)

    x = x + 1
    if x == 2001:
        sys.exit()
    


    delay(100)
