import turtle

class mainscreen:
#initilize the screen
 def __init__(self , width,height , color):
  self.width=width
  self.height=height
  self.color=color
 def screen(self):
  sc=turtle.Screen()
  sc.setup(self.height,self.width)
  sc.bgcolor(self.color)
  sc.exitonclick()
   