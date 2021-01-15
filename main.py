import random
#global alphabet
import turtle as tr
wn = tr.Screen()
wn.setup(width=1.0, height=1.0)

#lists
alphabet = ('b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','x','y','z')

#Turtle Setup
text = tr.Turtle() 
#text turtle
text.hideturtle()
text.penup()
#first course turtle
course1 = tr.Turtle() #Create and setup Course turtle 1
course1.penup()
course1.hideturtle()
course1.goto(0,200)
course1.pendown()
course1.speed("fastest")
#second course turtle
course2 = tr.Turtle() #Create and setup Course turtle 2
course2.penup()
course2.hideturtle()
course2.goto(0,130)
course2.pendown()
course2.speed("fastest")
#finish/startline turtle
st = tr.Turtle()
st.pencolor("yellow")
st.hideturtle()
st.pensize(5)
st.setheading(-90)
#first NPC turtle
npc1 = tr.Turtle()
npc1.penup()
npc1.hideturtle()
npc1.color("red")
npc1.goto(-20, 180)
npc1.speed("fastest")
#second NPC turtle
npc2 = tr.Turtle()
npc2.penup()
npc2.hideturtle()
npc2.color("blue")
npc2.goto(-50, 180)
npc2.speed("fastest")
#second NPC turtle
npc3 = tr.Turtle()
npc3.penup()
npc3.hideturtle()
npc3.color("orange")
npc3.goto(-20, 150)
npc3.speed("fastest")
#second NPC turtle
npc4 = tr.Turtle()
npc4.penup()
npc4.hideturtle()
npc4.color("green")
npc4.goto(-50, 150)
npc4.speed("fastest")
#player turtle
player = tr.Turtle()
player.penup()
player.goto(-80, 165)
player.hideturtle()

#variables
font_setup = ("Arial", 20, "normal")

global dist
dist = 5

#functions
def inicourseforward ():
  course1.forward(140)
  course2.forward(70)

def courseforward():
  course1.forward(100)
  course2.forward(100)

def courseforward2():
  course1.forward(210)
  course2.forward(70)

def courseright():
  course1.right(90)
  course2.right(90)
  course1.forward(100)
  course2.forward(100)

def courseleft():
  course1.left(90)
  course2.left(90)
  course1.forward(100)
  course2.forward(100)

def startline():
  st.penup()
  st.goto(0,197)
  st.pendown()
  st.forward(64)
  st.penup()
  st.goto(-150,197)
  st.pendown()
  st.forward(64)

def shownpc():
  npc1.st()
  npc2.st()
  npc3.st()
  npc4.st()
  player.st()

def playerright():
  player.setheading(0)
  player.forward(dist)

def playerleft():
  player.setheading(180)
  player.forward(dist)
  
def playerdown():
  player.setheading(270)
  player.forward(dist)

def playerup():
  player.setheading(90)
  player.forward(dist)

def randletter():
	global letter
	letter = alphabet[random.randint(0,21)]
	#print(letter)


def drawcourse():
  text.clear()
  inicourseforward()
  courseright()
  courseleft()
  courseforward()
  courseright()
  courseforward2()
  courseright()
  courseforward2()
  courseforward()
  courseright()
  courseleft()
  courseforward()
  courseforward()
  courseright()
  courseforward2()
  courseright()
  courseforward()
  inicourseforward()
  courseforward()
  startline()
  shownpc()
  randletter()

def playermovecheck():
	wn.onkeypress( speedincrease, letter)
	wn.onkey(playerright, "d")
	wn.onkey(playerleft, "a")
	wn.onkey(playerdown, "s")
	wn.onkey(playerup, "w")

def npccourse():
  wn.listen()
  x = 0
  while x < 35:
    npc1.forward(4)
    wn.onkeypress(playermovecheck, "d")
    npc2.forward(4)
    wn.onkeypress(playermovecheck, "d")
    npc3.forward(4)
    wn.onkeypress(playermovecheck, "d")
    npc4.forward(4)
    x += 1
  npc1.right(90)
  npc2.right(90)
  npc3.right(90)
  npc4.right(90)
  x = 0
  while x < 25:
    npc1.forward(4)
    npc2.forward(4)
    npc3.forward(4)
    npc4.forward(4)
    x += 1
  npc1.left(90)
  npc2.left(90)
  npc3.left(90)
  npc4.left(90)
  x = 0
  while x < 35:
    npc1.forward(4)
    npc2.forward(4)
    npc3.forward(4)
    npc4.forward(4)
    x += 1
  x = 0
  while x < 15:
    npc1.forward(4)
    npc2.forward(4)
    npc3.forward(4)
    npc4.forward(4)
    x += 1
  npc1.right(90)
  npc2.right(90)
  npc3.right(90)
  npc4.right(90)
  x = 0
  while x < 60:
    npc1.forward(4)
    npc2.forward(4)
    npc3.forward(4)
    npc4.forward(4)
    x += 1
  npc1.right(90)
  npc2.right(90)
  npc3.right(90)
  npc4.right(90)
  x = 0
  while x < 87:
    npc1.forward(4)
    npc2.forward(4)
    npc3.forward(4)
    npc4.forward(4)
    x += 1
  npc1.right(90)
  npc2.right(90)
  npc3.right(90)
  npc4.right(90)
  x = 0
  while x < 25:
    npc1.forward(4)
    npc2.forward(4)
    npc3.forward(4)
    npc4.forward(4)
    x += 1
  npc1.left(90)
  npc2.left(90)
  npc3.left(90)
  npc4.left(90)
  x = 0
  while x < 75:
    npc1.forward(4)
    npc2.forward(4)
    npc3.forward(4)
    npc4.forward(4)
    x += 1
  npc1.right(90)
  npc2.right(90)
  npc3.right(90)
  npc4.right(90)
  x = 0
  while x < 60:
    npc1.forward(4)
    npc2.forward(4)
    npc3.forward(4)
    npc4.forward(4)
    x += 1
  npc1.right(90)
  npc2.right(90)
  npc3.right(90)
  npc4.right(90)
  x = 0
  while x < 57:
    npc1.forward(4)
    npc2.forward(4)
    npc3.forward(4)
    npc4.forward(4)
    x += 1

def speedincrease():
	global dist
	dist = 15
	print("You've increased your speed!")



#Screen of text that says the game’s name
text.goto(-70,0) #Text go to middle of screen
text.write("Turtle Race", font=font_setup) #Type “Turtle Race” working name
text.goto(-105,-50) #goes to below text
text.write("Enter your name", font=font_setup) #types enter name

#input for Name
playername = input("Name: ") #input for players name
print("Welcome to Turtle Race. " + playername + ", click into the window and press 5 when ready") #prints welcome msg



#events
wn.listen()

wn.onkeypress(drawcourse, "5")
wn.onkeypress(npccourse, "6")


wn.mainloop()
