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

def newNPC(color, x, y, speed):
  t = tr.Turtle()
  t.penup()
  t.hideturtle()
  if color: t.color(color)
  t.goto(x, y)
  if speed: t.speed(speed)
  return t

class NPC_tracker:
    def __init__(self, turtles):
        self.turtles = turtles

    def forward(self, amount):
        for t in self.turtles:
            t.forward(amount)

    def left(self, amount):
        for t in self.turtles:
            t.left(amount)
            
    def right(self, amount):
        for t in self.turtles:
            t.right(amount)

NPCs = NPC_tracker([
    newNPC("red", -20, 180, "fastest"),
    newNPC("blue", -50, 180, "fastest"),
    newNPC("orange", -20, 150, "fastest"),
    newNPC("green", -50, 150, "fastest"),
])

player = newNPC(None, -80, 165, None)
player.penup()

#variables
font_setup = ("Arial", 20, "normal")

dist = 5

#functions
def inicourseforward():
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

#wn.onkeypress(playermovecheck, "d")

def npccourse():
  wn.listen()

  for _ in range(35):
    NPCs.forward(4)

  NPCs.right(90)
  
  for _ in range(25):
    NPCs.forward(4)

  NPCs.left(90)

  for _ in range(50):
    NPCs.forward(4)

  NPCs.right(90)
  
  for _ in range(60):
    NPCs.forward(4)

  NPCs.right(90)

  for _ in range(87):
    NPCs.forward(4)

  NPCs.right(90)

  for _ in range(25):
    NPCs.forward(4)

  NPCs.left(90)
  
  for _ in range(75):
    NPCs.forward(4)

  NPCs.right(90)
  
  for _ in range(60):
    NPCs.forward(4)
    
  NPCs.right(90)
  
  for _ in range(57):
    NPCs.forward(4)

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
