import numpy as np

class system:
    def __init__(self, bodies):
        self.bodies = bodies

    def findAccelerations(self):
        accs = []
        # calculate the accelerations for all of the bodies
        for body in self.bodies:
            others = []
            for body2 in self.bodies:
                if body != body2:
                    others.append(body2)
            accs.append(body.findAcceleration(others))
        return accs

    def integrate(self, n, dt):
        saved_pos = []
        for s in range(n):
            # use verlet integration/scheme to update the positions and velocities
            accs = self.findAccelerations()
            for i, body in enumerate(self.bodies):
                body.pos += body.vel * dt + accs[i] * dt**2 * 0.5
                saved_pos.append(body.pos)

            nextAccs = self.findAccelerations()

            for i, body in enumerate(self.bodies):
                body.vel += (nextAccs[i] + accs[i]) * dt * 0.5