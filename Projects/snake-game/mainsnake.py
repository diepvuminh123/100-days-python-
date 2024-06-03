import turtle
class Main:
        
    def setscreen(self, width, height, color):
        self.sc= turtle.Screen()
        self.sc.setup(width, height)  # Corrected to width, height
        self.sc.bgcolor(color)
        
    
    def setsnake(self, shape, color):
        self.sn = turtle.Turtle()
        self.sn.shape(shape)
        self.sn.color(color)
 

