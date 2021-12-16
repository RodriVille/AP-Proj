import turtle as turtle
import tkinter as tk
import random as random

#---Creating the screen---
wn = turtle.Screen()
wn.screensize()
wn.setup(width = 1.0, height = 1.0)#Making the screen the size of the monitor

asteroid_array = []

#---Creating the player shape---
player = turtle.Turtle()
wn.tracer(False)
#user_image = "Player.gif" #Image obtained from 'https://www.clipartkey.com/view/xbTRbb_8-bit-spaceship-png/'
#wn.addshape(user_image)
##wn.bgpic("Space.gif") #Image obtained from 'https://wallpaperaccess.com/pixel-space'
#player.shape(user_image)
#player.shape("triangle")
player.penup()
player.speed('fastest')
player.left(90)
player.goto(0, -300) #This moves the player to the starting position
wn.tracer(True)

#---Making the player follow the cursor to play---

'''
game = True#Parameter to test if game is over
def playerMove (player):
    while (game == True):#while game is not over, player will follow mouse
        cursor = turtle.getcanvas()
        player.goto(cursor.winfo_pointerx() -1920/2, -300)#Getting the cursor x position and moving the turtle to that coordinate
        break
    asteroids()
'''
def playerMove(player):
    wn.listen()
    player.ondrag(dragging)

def dragging(x, y): #https://www.techwithtim.net/tutorials/python-module-walk-throughs/turtle-module/drawing-with-mouse/
    player.ondrag(None)
    player.setheading(player.towards(x, y))
    player.goto(x, y)
    player.ondrag(dragging)

def asteroids():
    print('Watch out!')
    for i in range(0,3):
        asteroid = turtle.Turtle()
        asteroid.color('cyan')
        asteroid.speed("slowest")
        asteroid.left(90)
        wn.tracer(False)
        asteroid.penup()
        xasteroid = random.randint(-1920/2, 1920/2)
        asteroid.goto(xasteroid, 500)
        wn.tracer(True)
        asteroid_array.append(asteroid)
    for i in asteroid_array:
        i.bk(500)

def gameOver(asteroid_array, player):
    print("Poggers")
        
#---Program Start---
playerMove(player)
asteroids()

#---Open Window---

wn.update()
wn.mainloop()