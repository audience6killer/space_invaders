import turtle


class Scoreboard:
    def __init__(self, window_size: tuple):
        super().__init__()
        self.LIVES = 3
        self.window_size = window_size
        self.lives_list = [turtle.Turtle() for _ in range(self.LIVES)]
        x_margin = 150
        y_margin = 40
        count = 0
        space_between = 50
        for life in self.lives_list:
            life.penup()
            life.shape('assets/images/heart.gif')
            life.goto(x=self.window_size[0]/2 + space_between * count - x_margin,
                      y=self.window_size[1]/2 - y_margin)
            count += 1

    def decrease_lives(self) -> bool:
        self.lives_list[len(self.lives_list) - 1].goto(x=self.window_size[0], y=self.window_size[1])
        self.lives_list.pop()
        if not len(self.lives_list):
            return True
        else:
            return False

