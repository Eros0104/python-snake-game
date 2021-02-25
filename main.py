import turtle
import time
import random
from defaultObject import getObject
from snake import getSnake

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

head = getSnake()

food = getObject("square", "green", 0, 100) 

segments = []

sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("green")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score: 0 High score: 0", align="center", font=("ds-digital", 24, "normal"))

def go_up():
  if head.direction != "down":
    head.direction = "up"
def go_down():
  if head.direction != "up":
    head.direction = "down"
def go_left():
  if head.direction != "right":
    head.direction = "left"
def go_right():
  if head.direction != "left":
    head.direction = "right"
def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y+20)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y-20)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x-20)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x+20)

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

while True:
  wn.update()

  if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    for segment in segments:
      segment.goto(1000,1000)

    segments.clear()

    score = 0

    delay = 0.1

    sc.clear()
    sc.write("score: {} High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

  if head.distance(food) < 20:
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x,y)

    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("green")
    new_segment.penup()
    segments.append(new_segment)

    delay -= 0.001
    score += 10

    if score > high_score:
      hight_score = score
    sc.clear()
    sc.write("score: {} High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))

  for index in range(len(segments)-1,0,-1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x,y)

  if len(segments)>0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)

  move()

  for segment in segments:
    if segment.distance(head)<20:
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"

      for segment in segments:
        segment.goto(1000,1000)
      segments.clear()
      score = 0
      delay = 0.1

      sc.clear()
      sc.write("score: {} High Score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))
  time.sleep(delay)
wn.mainloop()