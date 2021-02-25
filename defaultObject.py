import turtle

def getObject(shape, color, x, y):
  obj = turtle.Turtle()
  obj.speed(0)
  obj.shape(shape)
  obj.color(color)
  obj.penup()
  obj.goto(x,y)

  return obj