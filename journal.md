# This is my journal
1. What did we do
2. What did I learn
3. What questions do I have

12 Apr 2020
1. In week 29 we expiremented more with python. Allowing us to explore our own means and ways of completing the work which can be from trying to brainstorm ideas or researching ideas that could work. Through this I was capable enough to complete some knew lines of code that I didnt understand before, one of the commands is "sys.exit()" which I found online. I needed a way of telling it to stop because it was finished, therefore I used a if statement followed by "sys.exit()" to stop the code when I wanted it to. I did all of this in the bears, the year is.., and celcius to farenheit challenges of week 29 in addition to bettering our covid-19 simulation code.

```.py
x = [random(0,500)] #a list, which is a collection of values
y = [random(0,500)] #a list, which is a collection of values h
h = [True, False]

def setup():
    size(500,500)
    #create random individuals
    for n in range (9):
        x.append(random(0,500))
        y.append(random(0,500))
        h.append(True)
        
def distance(x1, x2, y1, y2):
    a = (x1 - x2)
    b = (y1 - y2)
    c = sqrt(a**2 + b**2)
    return c

def draw():
    global x, y, h, n
    background(255)
    strokeWeight(2)

    #CREATING INDIVIDUALS
    for i in range (len(x)):
        if h[i] == True:
            fill(255)
        else:
            fill(255,0,0) #False
        circle(x[i], y[i], 40)
        
   #NEIGHBOURS 
        for n in range (len(x)):
            if n == i:
                continue
            d = distance(x[i], x[n], y[i], y[n])
            print(d)
            if d < 40 and (h[i] == False or h[n] == False):
                #Infection Happens
                h[i] = False
                h[n] = False
        
    #MOVING CIRCLES
    for m in range (len(x)):
        x[m] = x[m] + random(-10,10)
        y[m] = y[m] + random(-10,10)
    
            #boundaries conditions
        if (x[m] > 500):
            x[m] = 500
        if (x[m] < 0):
            x[m] = 0
        if (y[m] > 500):
            y[m] = 500
        if (y[m] < 0):
            y[m] = 0
    delay(50)
```

2. I learned how to better use google to research for computer science. Through repetition I am gettin the hang of undestanding how to be direct with google and get the answers out of it that I want. I knew how to do this for other subjects, but I learned for computer science, I just have to be very specific since thats how computers also think. And by working with computers, I have to adjust the way I think and research. I also learned how to use knew sequences such as sys.exit() to stop my code, and I learned how to calculate mathematics in my coding.


3. I wonder why the creators of python and other coding servers made it so that you have to get the code perfect for it to work. I undestand this allows for a better understanding of how computers work, but not easier. It makes it difficult because there might be small issues such as putting variables on the wrong side of the "=", this stops your code from working even though I believe it shouldnt since I dont see a possible alternative way of understanding this code.
