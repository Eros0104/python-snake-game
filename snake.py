from defaultObject import getObject

def getSnake():
   snake = getObject("square", "white", 0, 0)
   snake.direction = "stop"
   return snake