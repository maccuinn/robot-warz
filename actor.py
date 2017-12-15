from cocos.sprite import Sprite
from physics_action import PhysicsAction

class Actor(Sprite):
    """
    is an image and a position on the surface.
    """

    def __init__(self, config, position, *args):
        """
        :param config: values from item_config.py
        :param position: (int, int). the x and y coordinates
        """
        texture_name = '/'.join(['assets', 'textures',
                                 config['type'], config['texture']])
        super().__init__(texture_name)
        self.actor = Sprite(texture_name)
        self.size = config["size"]
        self.position = position
        self.x_velocity = 500
        self.y_velocity = 1
        self.do(PhysicsAction())

    def update(self, time):
        self.position = (self.position[0] + self.x_velocity * time, self.position[1])


