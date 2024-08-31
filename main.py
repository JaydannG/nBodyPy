import pygame as pg
from body import body
from system import system
import sys

# make the pygame window and set the size
pg.init()
window = pg.display.set_mode((1000, 1000))
pg.display.set_caption("n Body Simulation")

# create the planets
bodies = []

# y dir test
pluto = body(pos=(500.0, 900.0), mass=1.0, vel=(0, -.1))
bodies.append(pluto)

star = body(pos=(500.0, 100.0), mass=1.0, vel=(0, .1))
bodies.append(star)

# x dir test
# jupiter = body(pos=(900.0, 500.0), mass=1.0, vel=(-.1, 0))
# bodies.append(jupiter)

# neptune = body(pos=(100.0, 500.0), mass=1.0, vel=(.1, 0))
# bodies.append(neptune)

sys = system(bodies)

# number of steps
n = 1
dt = .1

while True:
    window.fill("black")

    for body in bodies:
        body.draw(window)
        sys.integrate(n, dt)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


    pg.display.flip()