import random
import turtle as tr
wn = tr.Screen()
wn.setup(width=1.0, height=1.0)

#lists
alphabet = ('b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','x','y','z')

def newNPC(color, x, y, speed):
  t = tr.Turtle()
  t.penup()
  t.hideturtle()
  t.goto(x, y)
  
  if color:
    t.color(color)

  if speed:
    t.speed(speed)

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

  def st(self):
    for t in self.turtles:
      t.st()

NPCs = NPC_tracker([
  newNPC("red", -20, 180, "fastest"),
  newNPC("blue", -50, 180, "fastest"),
  newNPC("orange", -20, 150, "fastest"),
  newNPC("green", -50, 150, "fastest"),
])

player = newNPC(None, -80, 165, None)
player.penup()

def quickTurtle(x, y, speed):
  t = tr.Turtle()
  t.penup()
  t.hideturtle()
  t.goto(x,y)
  t.pendown()
  t.speed(speed)
  return t

#Turtle Setup
text = tr.Turtle() 
text.hideturtle()
text.penup()

#first course turtle
courseTurtles = NPC_tracker([
  quickTurtle(0,200,"fastest"),
  quickTurtle(0,130,"fastest")
])

#finish/startline turtle
st = tr.Turtle()
st.pencolor("yellow")
st.hideturtle()
st.pensize(5)
st.setheading(-90)

#variables
font_setup = ("Arial", 20, "normal")

dist = 5

#functions
def inicourseforward():
  courseTurtles.turtles[0].forward(140)
  courseTurtles.turtles[1].forward(70)

def courseforward():
  courseTurtles.forward(100)

def courseforward2():
  courseTurtles.turtles[0].forward(210)
  courseTurtles.turtles[1].forward(70)

def courseright():
  courseTurtles.right(90)
  courseTurtles.forward(100)

def courseleft():
  courseTurtles.left(90)
  courseTurtles.forward(100)

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
  NPCs.st()
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
