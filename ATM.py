"""
While loops
Functions()
python argument
"""
#Simple Game
import turtle

#set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")







#Create a player
player = turtle.Turtle()
player.color('blue')
player.shape('turtle')
player.penup()
player.speed(0)

speed = 1

#Define function
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasedspeed():
    global speed
    speed += 1
    

#bind keyboard to functions
turtle.listen()
turtle.onkey(turnleft, 'Left')
turtle.onkey(turnright, 'Right')

turtle.onkey(increasedspeed, 'Up')


while True:
    player.forward(speed)
    if player.xcor() > 270 or player.xcor() < -270:
        player.right(180)
    if player.ycor() > 270 or player.ycor() < -270:
        player.right(180)






delay = raw_input("Press Enter to finish")



