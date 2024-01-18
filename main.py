import turtle

from spaceship import Spaceship, spaceship_bullets
from aliens import Aliens, aliens_bullets
from houses import Houses
from scoreboard import Scoreboard
# Screen settings
window_size = (650, 650)
screen = turtle.Screen()
screen.tracer(0)
screen.title('Space Invaders')
screen.setup(width=window_size[0], height=window_size[1])
screen.bgcolor('black')

# Add title image
screen.bgpic('assets/images/bg_1.gif')
screen.addshape('assets/images/logo_3.gif')
screen.addshape('assets/images/spaceship_2.gif')
screen.addshape('assets/images/alien_1.gif')
screen.addshape('assets/images/blast.gif')
screen.addshape('assets/images/red_shoot_2.gif')
screen.addshape('assets/images/brick.gif')
screen.addshape('assets/images/heart.gif')


game_logo = turtle.Turtle()
game_logo.shape('assets/images/logo_3.gif')
#game_logo.hideturtle()
game_logo.goto(x=game_logo.xcor(), y=window_size[1]/2 - 40)


spaceship_bullets.set_window_size(window_size)
aliens_bullets.set_window_size(window_size)

# Objects creation
my_ship = Spaceship(window_size)
my_house = Houses(window_size)
my_aliens = Aliens(window_size)
my_score = Scoreboard(window_size)

screen.listen()
screen.onkey(my_ship.move_left, 'Left')
screen.onkey(my_ship.move_right, 'Right')
screen.onkey(my_ship.shoot, 'Tab')

game_over = False

while not game_over:
    screen.update()
    if len(spaceship_bullets.projectiles):
        spaceship_bullets.update_projectiles()
        my_aliens.collision_detection(spaceship_bullets)
        my_house.collision_detection(spaceship_bullets)

    if len(aliens_bullets.projectiles):
        aliens_bullets.update_projectiles()
        my_house.collision_detection(aliens_bullets)
        if my_ship.collision_detection(aliens_bullets):
            game_over = my_score.decrease_lives()

    if len(aliens_bullets.projectiles) and len(spaceship_bullets.projectiles):
        aliens_bullets.collision_detection(spaceship_bullets)

    my_aliens.move()

    turtle.ontimer(my_aliens.shoot, t=500*my_aliens.NO_BULLETS)

game_over_msg = turtle.Turtle()
msg = 'Game Over'
game_over_msg.color('white')
game_over_msg.penup()
game_over_msg.write(arg=msg, move=False, align='center', font=('Ubuntu', 40, 'bold'))

screen.exitonclick()

