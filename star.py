import numpy as np
import random

class star:
    def __init__(self, pos, mass):
        self.pos = np.array(pos)
        self.mass = mass
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 

    def findAcceleration(self, bodies):
        return 0