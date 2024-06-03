import turtle

class Main:
    def __init__(self):
        self.snake = []
        self.direction = "stop"
        self.setup_screen()
        self.create_snake()
        self.sc.listen()
        self.sc.onkey(self.go_up, "Up")
        self.sc.onkey(self.go_down, "Down")
        self.sc.onkey(self.go_left, "Left")
        self.sc.onkey(self.go_right, "Right")
        self.move_snake()

    def setup_screen(self):
        self.sc = turtle.Screen()
        self.sc.setup(width=600, height=600)
        self.sc.bgcolor("black")
        self.sc.title("Snake Game")

    def create_snake(self):
        for i in range(3):
            self.add_segment((-20 * i, 0))

    def add_segment(self, position):
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def move_snake(self):
        while True:
            self.sc.update()
            self.move_segments()
            turtle.delay(100)

    def move_segments(self):
        for i in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[i-1].xcor()
            new_y = self.snake[i-1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.move_head()

    def move_head(self):
        if self.direction == "up":
            self.snake[0].setheading(90)
        if self.direction == "down":
            self.snake[0].setheading(270)
        if self.direction == "left":
            self.snake[0].setheading(180)
        if self.direction == "right":
            self.snake[0].setheading(0)
        self.snake[0].forward(20)

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"

snake_game = Main()
turtle.done()
