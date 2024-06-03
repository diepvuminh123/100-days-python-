import turtle
class snake:
 def __init__(self , shape , color):
  self.shape=shape
  self.color=color
 def createsnake(self):
  sn=turtle.Turtle()
  sn.shape(self.shape)
  sn.color(self.color)
