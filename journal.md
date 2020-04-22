# This is my journal
1. What did we do
2. What did I learn
3. What questions do I have

12 Apr 2020
1. In week 31 we took our COVID-19 simulation to the next level. I followed the instuctive videos that guided me to making my code a more complicated and more realisic simulation. I ran into many difficulites and problems during this week, and I had to fix a lot of these problems on my own by testing each parts of the code individually. I had to umderstand what I wanted each line of code to achieve, and deleted the lines that werent helpfull so that I could make the code simpler and easier to understand and work with. I achieved more than asked this week as I chose to build bar graphs for the recovered people, played around with the code to make it more realistic and more.

```.py
x = [random(0,500)] #a list, which is a collection of values
y = [random(0,500)] #a list, which is a collection of values h
h = ["healthy" , "sick"]
days = [-1,30]
infected = 0 #number of infected individuals
iteration = 0
recovered = 0

def bargraph():
    global infected, x, iteration
    line(0,500,500,500)
    healthy = len(x) - infected
    fill(255)
    rect(150, 520, 10*healthy, 10)
    fill(255,0,0)
    rect(150, 535, 10*infected, 10)
    fill(0,0,255)
    rect(150, 550, 10*recovered, 10)
    fill(0)
    text("Healthy {}".format(healthy),50,530)
    text("Recoverd {}".format(recovered),50,560)
    text("Sick {}".format(infected),50,545)
    text("Iteration No.{}".format(iteration),10,590)
    


def setup():
    size(500,600)
    #create random individuals
    for n in range (50):
        x.append(random(0,500))
        y.append(random(0,500))
        h.append("healthy")
        days.append(-1)
        
def distance(x1, x2, y1, y2):
    a = (x1 - x2)
    b = (y1 - y2)
    c = sqrt(a**2 + b**2)
    return c

  
def draw():
    global x, y, infected, iteration, recovered
    iteration = iteration + 1
    background(255)

    infected = 0
    
    for i in range(len(h)):
        if h[i] == "sick":
            infected = infected + 1
    bargraph()
        


    #CREATING INDIVIDUALS
    for i in range (len(x)):
        if h[i] == "healthy":
            fill(255)
        elif h[i] == "sick":
            fill(255,0,0) #"sick"        
        else:
            fill(0,0,255)
            
        circle(x[i], y[i], 40)
            
   #NEIGHBOURS 
        for n in range (len(x)):
            if n == i:
                continue
            d = distance(x[i], x[n], y[i], y[n])
            if d < 40 and h[i] == "sick" and h[n] == "healthy":
                h[n] = "sick"
                days[n] = 50

                
        
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
            
            
    #Change individual to recovered
    for i in range(len(h)):
        if h[i] == "sick":
            days[i] = days[i] - 1
            if days[i] == 0:
                h[i] = "recovered"
                recovered = recovered + 1

     
            
            #How to make a code that only allows the circles to touch, not allowed to go on top of eachother
    

    delay(50)
```

2. I learned how to create bar graphs in this code. Bar graphs are very usefull as it allows me to see the statstics of what is happening. I also learned how to work better with more complicated and next level coding as I had to fix mistakes and learn from them as lots of this week was finding your own way.


3. The next thing I would like to know is how to create a code that also allows the people to die from the corona virus, making it more realistic. This code would also detect the people that are high risk and it would make them have a higher chance of fatality.
