from turtle import Turtle, Screen, mainloop
from random import randint

def main():
  t = Turtle()
  s = Screen()

  s.tracer(0)                 # update turtle all at once
  s.bgcolor('black')
  t.speed(0)
  t.penup()

  colors: list = ['hotpink', 'orange', 'cyan']

  for dot in range(500):
    x = randint(-500, 500)
    y = randint(-500, 500)
    t.goto(x, y)
    size = randint(10, 75)

    if (x < -130):
      i = 0
    elif (x > 130):
      i = 2
    else:
      i = 1

    t.dot(size, colors[i])

  #s.mainloop()        # makes it more portable


main()
