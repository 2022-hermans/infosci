# This is my journal
1. What did we do
2. What did I learn
3. What questions do I have

18 Feb 2020
1. Today we created a chess board using a new code called "for n in range ()". This piece of code repeats the code listed under it for the number of time that is put within the brackets. This code also involves a optical illusion as by moving one of the repeting sequences, some square look bigger than other even though they are actually the same. And to show this slow progression we used the mouseClicked sequence which changes the amount it has moved every time you touch key pad.

```.py
offset = 50

def mouseClicked():
    global offset
    offset = offset + 1

def setup():
    size(500,500)
    background(255) #rgb
  
def draw():
    fill(0)
    stroke(0)
    y = 0
    for n in range (10):
        line (0,y,500,y)
        y = y + 50
        
    stroke(255)
    fill(0)
    y=0
    for n in range (5):
        x=0
        for n in range(5):
            square (x,y,50)
            x = x + 100
        y = y + 100
        
    y=50
    global offset
    for n in range (5):
        x = 0 + offset
        for n in range(5):
            square (x,y,50)
            x = x + 100
        y = y + 100
```

2. Today we learned a new piece of code " for n in range()". This is a repetition sequence which can make your code a lot more organized, simple and easier to understand and create. Using this code will probably save me a lot of time in the future, and through the practice of what we have already learned, I am slowly getting better at this whole coding proccess.


3. Is there a way to create a multiplied or exponentially increasing variable as now we know how to do a devided, added and subtracted but not multiplied or exponential?
