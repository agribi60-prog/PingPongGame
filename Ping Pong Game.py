# imported turtle module  
import turtle 
import time 

wind = turtle.Screen()#initialize the screen
wind.title("Ping Pong Game")#set the title of the window
wind.bgcolor("black")#set the background color of the window
wind.setup(width=800, height=600)#set the dimension of the window  
wind.tracer(0)#disable the window updates 

#madrab1
madrab1 = turtle.Turtle()#initialize turtle object(shape)
madrab1.speed(0)#set the speed of the animation
madrab1.shape("square")#set the shape of the turtle object
madrab1.color("blue")#set the color of the turtle object
madrab1.shapesize(stretch_wid=5, stretch_len=1)#stretches the shape to meet the size 
madrab1.penup()#stop the object from drawing lines
madrab1.goto(-350, 0)#set the position of the turtle object

#madrab2
madrab2 = turtle.Turtle()#initialize turtle object(shape)
madrab2.speed(0)#set the speed of the animation
madrab2.shape("square")#set the shape of the turtle object
madrab2.color("red")#set the color of the turtle object
madrab2.shapesize(stretch_wid=5, stretch_len=1)#stretches the shape to meet the size
madrab2.penup()#stop the object from drawing lines
madrab2.goto(350, 0)#set the position of the turtle object

#ball
ball = turtle.Turtle() 
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

#Initialize scores 
score1 = 0
score2 = 0


#score display
score = turtle .Turtle() 
score.speed(0) 
score.color("yellow")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0 player 2: 0", align="center",font=("courier",24,"normal"))
 

#functions
def madrab1_up():
    y = madrab1.ycor()#get the y coordinate of the madrab1
    y += 20#increase the y coordinate by 20
    madrab1.sety(y)#set the new y coordinate of the turtle object
def madrab1_down():
    y = madrab1.ycor()#get the y coordinate of the madrab1
    y -= 20#decrease the y coordinate by 20
    madrab1.sety(y)#set the new y coordinate of the turtle object



def madrab2_up():
    y = madrab2.ycor()#get the y coordinate of the madrab2
    y += 20#increase the y coordinate by 20
    madrab2.sety(y)#set the new y coordinate of the turtle object
def madrab2_down():
    y = madrab2.ycor()#get the y coordinate of the madrab2
    y -= 20#decrease the y coordinate by 20
    madrab2.sety(y)#set the new y coordinate of the turtle object



#keyboared bindings
wind.listen()#listen to the keyboared input
wind.onkeypress(madrab1_up, "w")#call the function when the key is pressed 
wind.onkeypress(madrab1_down, "s")#call the function when the key is pressed 
wind.onkeypress(madrab2_up, "u")#call the function when the key is pressed 
wind.onkeypress(madrab2_down, "d")#call the function when the key is pressed 


#main game loop
while True: 
    wind.update() #update the game screen to desplay the changes 

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) #update the ball's horizontal position (x-axis)
    ball.sety(ball.ycor() + ball.dy) #update the ball's vertical position (y-axis)

    # Border check
    if ball.ycor() > 290: 
        ball.sety(290) #keep the ball inside the top border 
        ball.dy *= -1  #reverse the vertical deriction (move dwonward)
 
    if ball.ycor() < -290:
        ball.sety(-290) #keep the ball inside the bottom border
        ball.dy *= -1   #reverse the vertical direction (move upward)
    
    if ball.xcor() > 390: #if the ball goes beyond the right border
       ball.goto(0, 0) #reset the ball position to the center of the screen
       ball.dx *= -1   #reverse the horizontal deriction (move leftward)
       score1 += 1  
       score.clear()
       score.write("player 1: {} player 2: {}".format(score1, score2) , align="center",font=("courier",24,"normal"))
    
    if ball.xcor() < -390: #if the ball goes beyond the left border
       ball.goto(0, 0) #reset the ball position to the center of the screen
       ball.dx *= -1  #reverse the horizontal deriction (move rightward)
       score2 += 1
       score.clear() 
       score.write("player 1: {} player 2: {}".format(score1, score2) , align="center",font=("courier",24,"normal"))
    
    #tasadom madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40  ):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40  ):
            ball.setx(-340)
            ball.dx *= -1 
    
    
    
    time.sleep(0.02) # add a small delay to control the speed of the game 



    