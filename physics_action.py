import cocos
from cocos.actions import Action


class PhysicsAction(Action):

    def step(self, dt):

        self.target.position = (self.target.position[0] + self.target.x_velocity * dt, self.target.position[1])






