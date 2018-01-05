from cocos.sprite import Sprite
from physics_action import PhysicsAction

from cocos.euclid import Vector3, Vector2
from cocos.collision_model import CircleShape


class Actor(Sprite):
    """
    is an image and a position on the surface.
    """

    def __init__(self, config, position, debug_label=None):
        """
        :param config: values from game_config.py
        :param position: (int, int). the x and y coordinates
        """
        texture_name = '/'.join(['assets', 'textures',
                                 config['type'], config['texture']])
        self.big = False
        self.dirty = True
        self.owner = None
        self.debug_label = debug_label
        super().__init__(texture_name)
        self.size = config["size"]
        rect = self.get_rect()
        self.scale_x = self.size[0]/rect.width
        self.scale_y = self.size[1]/rect.height
        self.coord = Vector3(*position)
        self.velocity = Vector3()
        self.do(PhysicsAction())
        self.cshape = CircleShape(Vector2(*self.coord.xy), self.size[0] / 2)

    def collide(self, others):
        pass
