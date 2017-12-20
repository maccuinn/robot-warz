from cocos.actions import Action

import config
from coord import Coord3d


NEAR_PLANE = 0
FAR_PLANE = 1000
NEAR_SCALE = 1
FAR_SCALE = 0.5
SCREEN_NEAR_Y = 10
SCREEN_FAR_Y = 490
SCREEN_NEAR_WIDTH = config.screen_size[0]
# todo should look into making this a percentage...possibly 50%?
SCREEN_FAR_WIDTH = config.screen_size[0] * 0.5


class PhysicsAction(Action):
    def step(self, dt):

        self.target.coord = self.target.velocity.scaled(dt).plus(self.target.coord)
        x, y, z = self.target.coord.tuple()
        if x > config.screen_size[0]:
            x = config.screen_size[0]
        if x < 0:
            x = 0
        if y > FAR_PLANE:
            y = FAR_PLANE
        if y < NEAR_PLANE:
            y = NEAR_PLANE
        self.target.coord = Coord3d(x, y, z)


        distance = (y - NEAR_PLANE) / FAR_PLANE

        self.target.scale = NEAR_SCALE - (distance * (NEAR_SCALE - FAR_SCALE))
        screen_width_diff = SCREEN_NEAR_WIDTH - SCREEN_FAR_WIDTH
        screen_y_diff = SCREEN_FAR_Y - SCREEN_NEAR_Y

        x_percent = x / SCREEN_NEAR_WIDTH
        width_at_distance = SCREEN_NEAR_WIDTH - distance * screen_width_diff
        distance_offset = (SCREEN_NEAR_WIDTH - width_at_distance) / 2
        x = width_at_distance * x_percent + distance_offset

        # TODO: apparent y distance travelled needs to decrease as distance increases
        y = (distance * screen_y_diff) + SCREEN_NEAR_Y

        rect = self.target.get_rect()  # get_rect might be slow
        rect.midbottom = x, y
        self.target.debug_label.element.text = '{0},{1}'.format(x,y)
        self.target.position = rect.center
