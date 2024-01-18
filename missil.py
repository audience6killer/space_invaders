import turtle


class Missil(turtle.Turtle):
    def __init__(self, y=0, x=0, alien=False, color='Red'):
        super().__init__()
        #self.shape('arrow')
        self.penup()
        #self.color('red')

        self.goto(x=x, y=y)
        self.is_alien = alien
        if not self.is_alien:
            self.setheading(90)
            self.shape('assets/images/red_shoot_2.gif')

        else:
            self.setheading(270)
            self.shape('assets/images/blast.gif')
        self.color = color


