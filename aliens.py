import turtle

ALIEN_WIDTH = 20 * 2


class Alien(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)


class Aliens:
    def __init__(self, window_size: tuple):
        """This class implements the creation and handling of the aliens grid that have to be destroyed"""
        self.window_size = window_size
        self.top_margin = 100
        self.rows_space = 30
        self.layers = []
        self.ROW_SPACE = 50
        self.COLUMN_SPACE = 15
        self.NO_LAYERS = 4
        self.ALIENS_PER_ROW = 6
        self.TOTAL_BLOCKS = self.NO_LAYERS * self.ALIENS_PER_ROW

    def create_layers(self):
        window_width = self.window_size[0]
        window_height = self.window_size[1]

        self.layers = [[Alien() for _ in range(self.ALIENS_PER_ROW)] for _ in range(self.NO_LAYERS)]

        top_y = (window_height / 2) - self.top_margin
        alien_grid_width = (self.ALIENS_PER_ROW * ALIEN_WIDTH +
                            (self.ALIENS_PER_ROW - 1) * self.COLUMN_SPACE - ALIEN_WIDTH)
        for row in self.layers:
            left_x = -alien_grid_width / 2
            for alien in row:
                alien.goto(x=left_x, y=top_y)
                left_x += ALIEN_WIDTH + self.COLUMN_SPACE

            top_y -= self.ROW_SPACE




