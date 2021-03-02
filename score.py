from defaultObject import getObject

def getScore():
    score = getObject("square", "green", 0, 260)
    score.hideturtle()

    return score

def writeScore(score = 0, high_score = 0):
    return "score: {} High score: {}".format(score, high_score)