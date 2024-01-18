import turtle
import random

from missil import Missil
from projectiles import OnScreenBullets

aliens_bullets = OnScreenBullets(max_on_screen=10)

ALIEN_WIDTH = 20 * 2


class Alien(turtle.Turtle):
    def __init__(self, id_: int):
        super().__init__()
        self.shape('assets/images/alien_1.gif')
        #self.color('green')
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.id_ = id_

class Aliens:
    def __init__(self, window_size: tuple):
        """This class implements the creation and handling of the aliens grid that have to be destroyed"""
        self.window_size = window_size
        self.top_margin = 100
        self.rows_space = 30
        self.aliens_grid = []
        self.ROW_SPACE = 50
        self.COLUMN_SPACE = 15
        self.NO_LAYERS = 4
        self.ALIENS_PER_ROW = 6
        self.NO_BULLETS = 1
        self.total_blocks = self.NO_LAYERS * self.ALIENS_PER_ROW

        self.create_layers()

        self.head = self.aliens_grid[0][5]
        self.tail = self.aliens_grid[0][0]
        self.move_right = True

    def create_layers(self):
        window_width = self.window_size[0]
        window_height = self.window_size[1]

        self.aliens_grid = [[Alien(id_=i) for i in range(self.ALIENS_PER_ROW)] for _ in range(self.NO_LAYERS)]

        top_y = (window_height / 2) - self.top_margin
        alien_grid_width = (self.ALIENS_PER_ROW * ALIEN_WIDTH +
                            (self.ALIENS_PER_ROW - 1) * self.COLUMN_SPACE - ALIEN_WIDTH)
        for row in self.aliens_grid:
            left_x = -alien_grid_width / 2
            for alien in row:
                alien.goto(x=left_x, y=top_y)
                left_x += ALIEN_WIDTH + self.COLUMN_SPACE

            top_y -= self.ROW_SPACE

    def collision_detection(self, bullet: OnScreenBullets):
        for missil in bullet.projectiles:
            self.collision_loop(missil, bullet)

    def collision_loop(self, missil, spaceship_bullet: OnScreenBullets):
        for row in self.aliens_grid:
            for alien in row:
                if alien.distance(missil) < 20:
                    self.total_blocks -= 1
                    if alien == self.head:
                        self.search_head()
                    elif alien == self.tail:
                        self.search_tail()
                    #alien.reset()
                    alien.goto(x=self.window_size[0], y=self.window_size[1])
                    row.remove(alien)
                    if not len(row):
                        self.aliens_grid.remove(row)
                    spaceship_bullet.remove_bullet(missil)
                    return

    def search_head(self):
        temp_head = self.head
        self.head = random.choice(random.choice(self.aliens_grid))
        for row in self.aliens_grid:
            for alien in row:
                if alien.id_ > self.head.id_ and alien is not temp_head:
                    self.head = alien

    def search_tail(self):
        temp_tail = self.tail
        self.tail = random.choice(random.choice(self.aliens_grid))
        for row in self.aliens_grid:
            for alien in row:
                if alien.id_ < self.tail.id_ and alien is not temp_tail:
                    self.tail = alien
    def shoot(self):
        if len(self.aliens_grid):
            rand_row = random.choice(self.aliens_grid)
            alien = random.choice(rand_row)
            new_missil = Missil(x=alien.xcor(), y=alien.ycor(), alien=True, color='Orange')
            aliens_bullets.add_new(new_missil)
            self.NO_BULLETS += 1

    def move(self):
        for row in self.aliens_grid:
            for alien in row:
                if self.move_right:
                    alien.goto(x=alien.xcor() + 1, y=alien.ycor())
                    if self.head.xcor() >= self.window_size[0] / 2 - 20:
                        self.move_right = False
                else:
                    alien.goto(x=alien.xcor() - 1, y=alien.ycor())
                    if abs(self.tail.xcor()) >= self.window_size[0] / 2 - 20:
                        self.move_right = True


