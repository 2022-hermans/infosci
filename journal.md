# This is my journal
1. What did we do
2. What did I learn
3. What questions do I have

18 Feb 2020
1. Today we created a virtual die on processing using python. We created a square within the plane which changed the number of dots in the rectangle every time we clicked the screen. We used the random feature to make sure that the value or number of dots on the die was randomized. We then altered the chances of getting one of the values, for me it was 3, and a friend had to identify which value had a higher chance of being chosen due to the change in the code. And I had to do the same but for someone else code.

```.py
def setup(): 
  size(600,600)
  background(255) #rgb

  
def draw():
    x=0
  #ellipse(200,200,50,50) #Top left
  #ellipse(200,300,50,50) #Mid Left
  #ellipse(200,400,50,50) #Bottom Left
  #ellipse(300,300,50,50) #Mid
  #ellipse(400,200,50,50) #Top Right
  #ellipse(400,400,50,50) #Bottom Right
  #ellipse(400,300,50,50) #Mid Right

def mouseClicked():
    strokeWeight(20)
    fill(255)
    stroke(0)
    rect(100,100,400,400,50)
    stroke(255,0,0)
    fill(255,0,0)
    n=random(0,6)
    
    if 0<=n<1:
        ellipse(300,300,50,50) #Mid
      
    if 1<=n<2:
        ellipse(200,300,50,50) #Mid Left
        ellipse(400,300,50,50) #Mid Right
        
    if 2<=n<3:
        ellipse(200,200,50,50) #Top left
        ellipse(400,400,50,50) #Bottom Right
        ellipse(300,300,50,50) #Mid
        
    if 3<=n<4:
        ellipse(200,200,50,50) #Top left
        ellipse(400,400,50,50) #Bottom Right
        ellipse(200,400,50,50) #Bottom Left
        ellipse(400,200,50,50) #Top Right
        
    if 4<=n<5:
        ellipse(200,200,50,50) #Top left
        ellipse(400,400,50,50) #Bottom Right
        ellipse(200,400,50,50) #Bottom Left
        ellipse(400,200,50,50) #Top Right
        ellipse(300,300,50,50) #Mid
        
    if 5<=n<=6:
        ellipse(200,200,50,50) #Top left
        ellipse(200,300,50,50) #Mid Left
        ellipse(200,400,50,50) #Bottom Left
        ellipse(400,200,50,50) #Top Right
        ellipse(400,400,50,50) #Bottom Right
        ellipse(400,300,50,50) #Mid Right
```

2. Today we learned how to use new commands such as, if, stroke and strokeWeight. We also learned how to put these commands that we already learned in harder and more advanced code. We are still learning how to use the basics and practice is what is allowing me to get better.

3. What are the main commands that we will be using this year?
