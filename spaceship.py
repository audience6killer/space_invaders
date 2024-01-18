import turtle
from projectiles import OnScreenBullets
from missil import Missil

spaceship_bullets = OnScreenBullets(max_on_screen=3)


class Spaceship(turtle.Turtle):
    def __init__(self, window_size: tuple):
        """This class implements the spaceship that will shoot the
        aliens"""
        super().__init__()
        self.window_size = window_size
        #self.shape('triangle')
        self.shape('assets/images/spaceship_2.gif')
        self.color('white')
        self.setheading(90)
        self.penup()
        self.x_margin = 10

        self.lives = 3

        ship_stretch_wid = 2
        ship_stretch_len = 2
        self.ship_length = ship_stretch_len * 20
        self.ship_width = ship_stretch_wid * 20
        self.shapesize(stretch_wid=ship_stretch_wid,
                       stretch_len=ship_stretch_len)
        margin = 30
        self.initial_position = (0, (-window_size[1]/2)+margin)
        self.goto(y=self.initial_position[1], x=self.initial_position[0])

    def move_right(self):
        if abs(self.xcor() + 20 + self.x_margin) < (self.window_size[0] - self.ship_length)/2:
            new_x = self.xcor() + 20
            self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        if abs(self.xcor() - 20 - self.x_margin) < (self.window_size[0] - self.ship_length)/2:
            new_x = self.xcor() - 20
            self.goto(x=new_x, y=self.ycor())

    def shoot(self):
        new_missil = Missil(x=self.xcor(), y=self.ycor())
        spaceship_bullets.add_new(new_missil)

    def collision_detection(self, bullet: OnScreenBullets) -> bool:
        for missil in bullet.projectiles:
            if self.distance(missil) < 20:
                self.goto(x=self.window_size[0], y=self.window_size[1])
                bullet.remove_bullet(missil)
                self.goto(x=self.initial_position[0], y=self.initial_position[1])
                return True

        return False



