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
        self.size = config["size"]
        rect = self.get_rect()
        self.scale_x = self.size[0]/rect.width
        self.scale_y = self.size[1]/rect.height
        rect = self.get_rect()
        rect.midbottom = position
        self.position = rect.center
        self.x_velocity = 0
        self.y_velocity = 0
        self.do(PhysicsAction())

    def update(self, time):
        self.position = (self.position[0] + self.x_velocity * time, self.position[1])



