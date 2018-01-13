from cocos.actions import Action

import config
from game_config import game_board
from cocos.euclid import Vector3, Vector2
from cocos.collision_model import CircleShape


NEAR_PLANE = 0
FAR_PLANE = game_board["size"][1]
NEAR_SCALE = 1
FAR_SCALE = 0.5
SCREEN_NEAR_Y = 10
SCREEN_FAR_Y = 490
SCREEN_NEAR_WIDTH = game_board["size"][0]
SCREEN_FAR_WIDTH = SCREEN_NEAR_WIDTH * 0.5


class PhysicsAction(Action):
    """
    Applies the physics for each frame for each actor
    """

    def start(self):
        """
        runs one frame at the beginning
        """
        self.step(0)

    def step(self, dt):
        """
        runs one frame for each actor of the game
        :param dt: delta time: the difference in time between previous frame and next frame
        """

        # if not moving, or not changed
        if not (self.target.velocity or self.target.dirty):
            return

        # reset dirty to false
        self.target.dirty = False

        # adding the change in location based on velocity
        self.target.coord = self.target.velocity * dt + self.target.coord
        x, y, z = self.target.coord.xyz

        # check to see if target goes off screen and, if so, set appropriate coords
        if self.target.velocity:
            if x > config.screen_size[0]:
                x = config.screen_size[0]
            if x < 0:
                x = 0
            if y > FAR_PLANE:
                y = FAR_PLANE
            if y < NEAR_PLANE:
                y = NEAR_PLANE

            self.target.coord = Vector3(x, y, z)

        # distance is the percentage of distance between the near and far planes
        distance = (y - NEAR_PLANE) / FAR_PLANE

        # calculates the scale of the actor
        self.target.scale = NEAR_SCALE - (distance * (NEAR_SCALE - FAR_SCALE))

        # right now this is for debugging
        # todo create effect for when actor is hit
        if self.target.big:
            self.target.scale *= 2

        # used to calculate the location on the x axis
        screen_width_diff = SCREEN_NEAR_WIDTH - SCREEN_FAR_WIDTH

        # used to calculate the location on the y axis
        screen_y_diff = SCREEN_FAR_Y - SCREEN_NEAR_Y

        # used to calculate where they should appear on the x axis
        x_percent = x / SCREEN_NEAR_WIDTH

        # width of the game field at the distance you are at
        width_at_distance = SCREEN_NEAR_WIDTH - distance * screen_width_diff

        # offset for x based on the distance on y
        distance_offset = (SCREEN_NEAR_WIDTH - width_at_distance) / 2

        # calculates the x value for position.
        x = width_at_distance * x_percent + distance_offset

        # TODO: apparent y distance travelled needs to decrease as distance increases
        # calculates the y value for position.
        y = (distance * screen_y_diff) + SCREEN_NEAR_Y

        # get the rect to get where the actor's feet are
        rect = self.target.get_rect()

        rect.midbottom = x, y + z * self.target.scale

        # set up debug
        if self.target.debug_label is not None:
            self.target.debug_label.element.text = '{0},{1}'.format(x, y)

        # position is position of rect on screen.
        self.target.position = rect.center

        # sorting actors along the y axis. if y value is higher, actor should appear behind
        if self.target.velocity.y != 0:
            self.target.parent.remove(self.target)
            # inverse y coordinate to make it smaller for sorting.
            self.target.parent.add(self.target, -self.target.coord.y)

        self.target.cshape = CircleShape(Vector2(*self.target.coord.xy), self.target.size[0] / 2)

