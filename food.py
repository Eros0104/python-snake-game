from defaultObject import getObject
import random

def getFood():
   return getObject("square", "red", 0, 100)

def getFoodCoordinate():
   return random.randint(-14, 14) * 20