from missil import Missil


class OnScreenBullets:
    def __init__(self, max_on_screen=10):
        self.projectiles = []
        self.MAX_ON_SCREEN = max_on_screen
        self.window_size = (0, 0)

    def set_window_size(self, window_size: tuple):
        self.window_size = window_size

    def add_new(self, missil: Missil):
        if len(self.projectiles) <= self.MAX_ON_SCREEN:
            self.projectiles.append(missil)
        else:
            missil.reset()
            missil.goto(x=self.window_size[0], y=self.window_size[1])


    def remove_bullet(self, missil: Missil):
        missil.goto(x=self.window_size[0], y=self.window_size[1])
        #missil.reset()
        self.projectiles.remove(missil)

    def update_projectiles(self):
        for missil in self.projectiles:
            if not missil.is_alien:
                missil.forward(3)
            else:
                missil.forward(3)

            if abs(missil.ycor()) > self.window_size[1] / 2:
                self.remove_bullet(missil)

    def collision_detection(self, bullet):
        for missil in bullet.projectiles:
            self.collision_loop(missil, bullet)

    def collision_loop(self, missil, bullet):
        for my_bullet in self.projectiles:
            if my_bullet.distance(missil) < 20:
                self.remove_bullet(my_bullet)
                bullet.remove_bullet(missil)
                return

