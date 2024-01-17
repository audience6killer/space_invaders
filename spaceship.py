import turtle


class Spaceship(turtle.Turtle):
    def __init__(self, window_size: tuple):
        """This class implements the spaceship that will shoot the
        aliens"""
        super().__init__()
        self.window_size = window_size
        self.shape('triangle')
        self.color('white')
        self.setheading(90)
        self.penup()
        self.x_margin = 10

        ship_stretch_wid = 2
        ship_stretch_len = 2
        self.ship_length = ship_stretch_len * 20
        self.ship_width = ship_stretch_wid * 20
        self.shapesize(stretch_wid=ship_stretch_wid,
                       stretch_len=ship_stretch_len)
        margin = 30
        self.goto(y=(-window_size[1]/2)+margin, x=0)

    def move_right(self):
        if abs(self.xcor() + 20 + self.x_margin) < (self.window_size[0] - self.ship_length)/2:
            new_x = self.xcor() + 20
            self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        if abs(self.xcor() - 20 - self.x_margin) < (self.window_size[0] - self.ship_length)/2:
            new_x = self.xcor() - 20
            self.goto(x=new_x, y=self.ycor())

