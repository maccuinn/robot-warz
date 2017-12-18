import cocos
from cocos.actions import Action


class PhysicsAction(Action):
    def step(self, dt):

        self.target.coord = self.target.velocity.scaled(dt).plus(self.target.coord)
        rect = self.target.get_rect()  # get_rect might be slow
        rect.midbottom = self.target.coord.tuple()[:2]
        self.target.position = rect.center






