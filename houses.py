import turtle

from projectiles import OnScreenBullets


class Turtle(turtle.Turtle):
    def __init__(self, id_: int):
        super().__init__()
        self.id = id_


class House:
    def __init__(self):
        self.blocks = [Turtle(id_=i) for i in range(5)]
        self.HOUSE_BLOCKS = 5
        for block in self.blocks:
            block.shape('assets/images/brick.gif')
            block.color('blue')
            block.penup()
            block.shapesize(stretch_wid=1, stretch_len=1)

        # We place the blocks to form a house
        self.blocks[0].goto(x=-20, y=20 / 2)
        self.blocks[1].goto(x=-20, y=20 / 2 + 20)
        self.blocks[2].goto(x=0, y=20 / 2 + 20 * 2)
        self.blocks[3].goto(x=2*20-20, y=20 / 2 + 20)
        self.blocks[4].goto(x=2*20-20, y=20 / 2)

    def x_move(self, change: int):
        for block in self.blocks:
            block.goto(x=block.xcor() + change, y=block.ycor())

    def y_move(self, change: int):
        for block in self.blocks:
            block.goto(x=block.xcor(), y=block.ycor() + change)


class Houses:
    def __init__(self, window_size: tuple):
        self.window_size = window_size
        self.NO_HOUSES = 5
        self.total_blocks = self.NO_HOUSES * 5
        self.houses = [House() for _ in range(self.NO_HOUSES)]
        x_increment = 0
        window_width = window_size[0]
        x_left = window_width / 2 - 65
        for house in self.houses:
            house.x_move(-x_left+x_increment)
            house.y_move(-150)
            x_increment += window_width / self.NO_HOUSES

    def collision_detection(self, bullet: OnScreenBullets):
        for missil in bullet.projectiles:
            self.collision_loop(missil, bullet)

    def collision_loop(self, missil, bullet: OnScreenBullets):
        for house in self.houses:
            for block in house.blocks:
                if block.distance(missil) < 20:
                    self.total_blocks -= 1
                    block.goto(x=self.window_size[0], y=self.window_size[1])
                    bullet.remove_bullet(missil)
                    return

