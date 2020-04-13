x = 1

def calculations(x):
    a = x * 1.8
    b = a + 32
    return b

  
def draw():
    global x
    background(255)
    strokeWeight(2)
    c = calculations(x)
    print(x),("C are"),(c),("F")
    x = x + 1


    
    delay(50)
