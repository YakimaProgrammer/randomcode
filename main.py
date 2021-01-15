import random
import turtle as tr
wn = tr.Screen()
wn.setup(width=1.0, height=1.0)

#list of charecters that may be used to boost speed
alphabet = ['b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','x','y','z']

#these classes and functions make it easier to work with turtles
class NPC_tracker:
  def __init__(self, turtles):
    "Accepts an arbitrarily long list of turtle objects and allows you to move them like one turtle! *Many methods of the Turtle class are unneeded and go unimplemented in this helper*"
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

def quickTurtle(x, y, speed):
  "Creates a turtle at the given position with the given speed. The pen starts down and the turtle is hidden."
  t = tr.Turtle()
  t.penup()
  t.hideturtle()
  t.goto(x,y)
  t.pendown()
  t.speed(speed)
  return t

def newNPC(color, x, y, speed):
  "Creates a turtle with the color, position and speed given. The pen starts up and the turtle is hidden. Color and speed are optional. Pass any false-y value to have these properties remain as the default."
  t = tr.Turtle()
  t.penup()
  t.hideturtle()
  t.goto(x, y)
  
  if color:
    t.color(color)

  if speed:
    t.speed(speed)

  return t

#functions that make the game possible!
def initcourseForward():
  courseTurtles.turtles[0].forward(140)
  courseTurtles.turtles[1].forward(70)

def courseForward():
  courseTurtles.forward(100)

def courseForward2():
  courseTurtles.turtles[0].forward(210)
  courseTurtles.turtles[1].forward(70)

def courseRight():
  courseTurtles.right(90)
  courseTurtles.forward(100)

def courseLeft():
  courseTurtles.left(90)
  courseTurtles.forward(100)

def startLine():
  st.penup()
  st.goto(0,197)
  st.pendown()
  st.forward(64)
  st.penup()
  st.goto(-150,197)
  st.pendown()
  st.forward(64)

def showPC():
  NPCs.st()
  player.st()

def playerRight():
  player.setheading(0)
  player.forward(game_state["dist"])

def playerLeft():
  player.setheading(180)
  player.forward(game_state["dist"])
  
def playerDown():
  player.setheading(270)
  player.forward(game_state["dist"])

def playerUp():
  player.setheading(90)
  player.forward(game_state["dist"])

def drawCourse():
  text.clear()
  initcourseForward()
  courseRight()
  courseLeft()
  courseForward()
  courseRight()
  courseForward2()
  courseRight()
  courseForward2()
  courseForward()
  courseRight()
  courseLeft()
  courseForward()
  courseForward()
  courseRight()
  courseForward2()
  courseRight()
  courseForward()
  initcourseForward()
  courseForward()
  startLine()
  showPC()

def playerMoveCheck():
  wn.onkeypress( speedincrease, game_state["random_letter"])
  wn.onkey(playerRight, "d")
  wn.onkey(playerLeft, "a")
  wn.onkey(playerDown, "s")
  wn.onkey(playerUp, "w")

def npcCourse():
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
  game_state["dist"] = 15
  print("You've increased your speed!")

#with that out of the way, let's make some objects!

#these are the first four NPCs that you race against
NPCs = NPC_tracker([
  newNPC("red", -20, 180, "fastest"),
  newNPC("blue", -50, 180, "fastest"),
  newNPC("orange", -20, 150, "fastest"),
  newNPC("green", -50, 150, "fastest"),
])

#add a player
player = newNPC(None, -80, 165, None)
player.penup()

#create a text object so we can display messages faster!
text = tr.Turtle() 
text.hideturtle()
text.penup()

#these turtles help us draw the course
courseTurtles = NPC_tracker([
  quickTurtle(0,200,"fastest"),
  quickTurtle(0,130,"fastest")
])

#this turtle draws the start and finish line
st = tr.Turtle()
st.pencolor("yellow")
st.hideturtle()
st.pensize(5)
st.setheading(-90)

#variables are nice. Let's add a couple of them
FONT_SETUP = ("Arial", 20, "normal")

#these values represent how far the player should move and what keys they need to push to move faster
game_state = {
  "dist": 5,
  "random_letter": random.choice(alphabet)
}

#draw the opening scene
text.goto(-70,0) #Text go to middle of screen
text.write("Turtle Race", font=FONT_SETUP) #Types "Turtle Race"
text.goto(-105,-50) #goes to below text
text.write("Enter your name", font=FONT_SETUP) #requests that the user inputs a name in the console

print("Welcome to Turtle Race. " + input("Name: ") + ", click into the window and press 5 when ready") #prints welcome msg

#what? All that work and you actually want to PLAY the game? Fine. I'll listen for your keypresses.
wn.listen()

wn.onkeypress(playerMoveCheck, "d")
wn.onkeypress(drawCourse, "5")
wn.onkeypress(npcCourse, "6")

wn.mainloop()
