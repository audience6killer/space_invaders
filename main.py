import turtle

from spaceship import Spaceship
from aliens import Aliens
from houses import Houses

# Screen settings
window_size = (650, 650)
screen = turtle.Screen()
screen.tracer(0)
screen.title('Space Invaders')
screen.setup(width=window_size[0], height=window_size[1])
screen.bgcolor('black')

# Objects creation
my_ship = Spaceship(window_size)
my_house = Houses(window_size)
my_aliens = Aliens(window_size)
my_aliens.create_layers()

screen.listen()
screen.onkey(my_ship.move_left, 'Left')
screen.onkey(my_ship.move_right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()

