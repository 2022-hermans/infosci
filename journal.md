# This is my journal
1. What did we do
2. What did I learn
3. What questions do I have

6 Apr 2020
1. Today we used processing to make a python code. This code included making the first 2 steps of the final product being the simulation of the spread of covid-19. The first step was to find a way to represent individuals which may or may not have covid-19. Using abstraction we understand that for our purpose of simulating the spread of the disease, the only characteristic necessary to show would be if the person is infected which we can do by changing the colour of the representation. There is no need to show race, hair colour, eye colour or anything like that. Therefore we went with a simple circle with the idea to change the colour if infected. The next step was representing a community, we did this by making 10 circles representing 10 people and allowing them to move around the space, we used "for loop" sequences for this.

```.py
x = [random(0,500)] #a list, which is a collection of values
y = [random(0,500)] #a list, which is a collection of values 

def setup():
    size(500,500)
    #create random individuals
    for n in range (9):
        x.append(random(0,500))
        y.append(random(0,500))
  
def draw():
    global x, y
    background(255)
    strokeWeight(2)
    
    #create 1st Individual
    for i in range (10):
        circle(x[i], y[i], 40)
        x[i] = x[i] + random(-10,10)
        y[i] = y[i] + random(-10,10)
        
            #boundaries conditions
        if (x[i] > 500):
            x[i] = 500
        if (x[i] < 0):
            x[i] = 0
        if (y[i] > 500):
            y[i] = 500
        if (y[i] < 0):
            y[i] = 0
           
    delay(100)
```

2. Today I practiced using "for loop" sequences, which is necessary for me to better understand how and when to use the sequence. I also learned a new sequance, ".append" which I used in the setup function. It is a way of adding values to a list for an already defined variable. This sequence is very handy for not having to manually imput values for the variables into a list. A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item, (Tagliaferri, 2016).

3. How do I make a code that only allows the circles to touch eachother, but doesnt allow them to go on top of eachother?
