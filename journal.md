# This is my journal
1. What did we do
2. What did I learn
3. What questions do I have

4 Feb 2020
1. Today we explored and played around with the Python language on proccessing. I created circles that would pop up wherever I wanted it to. Below is the code that I made today which puts a circle where you click, fills it with a random colour and puts the word "Chihoo" in black on top of that circle.

```.py
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
    
    print (x,y)
```

2. Today we learned how to use different commands within proccessing, including; Random, textSize, text, fill, (variables), print, textAlign, size, and background. These new code commands and how to use them has tought me the essence of coding, using them has allowed me to undestand how the computer uses codes and the basic rules one must follow when coding such as: the computer goes down in code, therefore the first command must be at the top.
3. By the end of the course, what will we be able to code and make?
