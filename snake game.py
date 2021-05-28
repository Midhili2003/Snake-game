import turtle
import time
import random

delay = 0.1

#scoring
score = 0
best_score = 0


#set up the screen
sc =  turtle.Screen()
sc.title("Snake Game Powered By Midhili")
sc.bgcolor("black")
sc.setup(width=600, height=600)
sc.tracer(0)    #turns off the screen updates

#Snake head
snake_head = turtle.Turtle()
snake_head.speed(0) #0 is the fastest animation speed
snake_head.shape("circle")
snake_head.color("green")
snake_head.penup() #so that nothing is drawn by the turtle module
snake_head.goto(0,0) #to set the head at center of the screen in  the beginning of the game
snake_head.direction = "stop"

#Snake head
snake_food = turtle.Turtle()
snake_food.speed(0) #0 is the fastest animation speed
snake_food.shape("triangle")
snake_food.color("magenta")
snake_food.penup() #so that nothing is drawn by the turtle module
snake_food.goto(0,100) #to set the head at center of the screen in  the beginning of the game

segs = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Score: 0   Best Score: 0",align="center", font=("Times New Roman", 26, "italic"))


#functions
def move_up():
    snake_head.direction = "up"

def move_down():
    snake_head.direction = "down"

def move_left():
    snake_head.direction = "left"

def move_right():
    snake_head.direction = "right"


def to_move():
    if snake_head.direction == "up":
        y_pos = snake_head.ycor()
        snake_head.sety(y_pos + 20)

    if snake_head.direction == "down":
        y_pos = snake_head.ycor()
        snake_head.sety(y_pos - 20)

    if snake_head.direction == "left":
        x_pos = snake_head.xcor()
        snake_head.setx(x_pos - 20)

    if snake_head.direction == "right":
        x_pos = snake_head.xcor()
        snake_head.setx(x_pos + 20)
        
#keyboard bindings
sc.listen()
sc.onkeypress(move_up, "i")
sc.onkeypress(move_down, "k")
sc.onkeypress(move_left, "j")
sc.onkeypress(move_right, "l")


#Main game loop

while True:     #repeats the loop over and over and over again
    sc.update()

    #check for border collisions
    if snake_head.xcor()>290 or snake_head.xcor()<-290 or snake_head.ycor()>290 or snake_head.ycor()<-290:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = "stop"

        # Hide the segments
        for seg in segs:
            seg.goto(990,990)

        # to clear the segments
        segs.clear()

        #Reset the score
        score = 0

        #Set the delay
        delay = 0.1

        #updating the screen
        pen.clear()
        pen.write("score: {}   Best_score: {}".format(score, best_score), align = "center", font=("Times New Roman", 26, "italic"))
        
            
        
        
    
    #check for collision with the food
    if snake_head.distance(snake_food) < 20:
        #move the food to random position
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        snake_food.goto(x, y)

        #add a segment to the snake's body
        add_seg = turtle.Turtle()
        add_seg.speed(0)
        add_seg.shape("circle")
        add_seg.color("gold")
        add_seg.penup()
        segs.append(add_seg)

        #shorten the delay
        delay -= 0.0001

        # increment the score
        score += 10
        if score > best_score:
            best_score = score
        pen.clear()
        pen.write("score: {}   Best_score: {}".format(score, best_score), align = "center", font=("Times New Roman", 26, "italic"))
        

    #Move the end segments first in reverse order
    for i in range(len(segs)-1, 0, -1):
        x = segs[i - 1].xcor()
        y = segs[i - 1].ycor()
        segs[i].goto(x, y)

    #Move segment 0 to where the head is
    if len(segs) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segs[0].goto(x, y)
        
    to_move()

    #check for body collisions
    for seg in segs:
        if seg.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction = "stop"

            #Hide the segments
            for seg in segs:
                seg.goto(990,990)

            #clear the segments
            segs.clear()

            
            #Reset the score
            score = 0

            #set the delay
            delay  = 0.1
            
            #Update the screen
            pen.clear()
            pen.write("score: {}   Best_score: {}".format(score, best_score), align = "center", font=("Times New Roman", 26, "italic"))

    time.sleep(delay)

sc.mainloop()  # it will keep the window open for us
