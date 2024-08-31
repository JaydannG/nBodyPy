import pygame as pg
from body import body
from system import system

# make the pygame window and set the size
pg.init()
window = pg.display.set_mode((500, 500))
pg.display.set_caption("n Body Simulation")

# create the planets
bodies = []

# y dir test
pluto = body(pos=(250.0, 250.0), mass=1.0, vel=(.1, -.1))
bodies.append(pluto)

star = body(pos=(100.0, 300.0), mass=1.0, vel=(-.1, .1))
bodies.append(star)

# x dir test
jupiter = body(pos=(300.0, 200.0), mass=1.0, vel=(-.1, -.1))
bodies.append(jupiter)

neptune = body(pos=(400.0, 350.0), mass=1.0, vel=(.1, .1))
bodies.append(neptune)

sys = system(bodies)

saved_pos = []

# number of steps
n = 1
dt = .1

while True:
    window.fill("black")

    for body in bodies:
        for i in range(len(saved_pos)):
            pg.draw.line(window, body.color, saved_pos[i], saved_pos[i])
        body.draw(window)
        sys.integrate(n, dt)
        body.saved_pos.append((body.pos[0], body.pos[1]))
        body.draw_line(window)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


    pg.display.flip()