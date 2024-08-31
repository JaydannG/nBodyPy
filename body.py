import numpy as np
import pygame as pg
import math
import random

class body:
    # constructer for the bodies
    # takes a position in the form of a vector (array, [x, y])
    # takes a mass (in kg)
    def __init__(self, pos, mass, vel):
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.mass = mass
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 

    # draws the body in the pygame window
    def draw(self, surface):
        pg.draw.circle(surface, self.color, (self.pos[0], self.pos[1]), 7)

    # calculates the acceleration of this body based on the other bodies
    def findAcceleration(self, bodies, G=1.0):
        acc = np.zeros(2)

        for body in bodies:
            if body != self:
                # find the distance between the bodies and use it to calculate the force between them 
                r = self.pos - body.pos
                F = (G * self.mass * body.mass) / np.linalg.norm(r)**2

                # calculate the angle of the force and use it to determine the components of the force
                angle = math.atan(r[1] / (r[0] + 1e-10))
                Fx = F * np.cos(angle)
                Fy = F * np.sin(angle)

                # switch the direction of the force based on the positions of the bodies
                if (self.pos[0] > body.pos[0]): Fx = -Fx
                if (self.pos[1] > body.pos[1]): Fy = -Fy

                # calculate the acceleration based on the forces
                acc[0] = Fx / self.mass
                acc[1] = Fy / self.mass

        return acc