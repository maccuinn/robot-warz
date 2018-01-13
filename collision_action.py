from cocos.actions import Action, RotateBy

import config
from game_config import game_board
from cocos.euclid import Vector3, Vector2
from cocos.collision_model import CircleShape, CollisionManagerGrid

# todo create a collision action which game layer will do and collect all the collidables and then
# todo do them in step method of collision action


class CollisionAction(Action):
    """
    Finds all the items that collided and takes appropriate action
    """
    def init(self):
        """
        collision_manager:
        """
        width, height = game_board["size"]
        self.collision_manager = CollisionManagerGrid(0, width, 0, height, width // 10, height // 10)

    def start(self):
        """
        runs once per frame
        """
        self.step(0)

    def step(self, dt):
        """

        :param dt: delta time: difference in time between previous frame and next frame
        """
        cm = self.collision_manager

        # add each player to the collision manager. If player is big, set flag to dirty
        # and reset player to small
        for player in self.target.players:
            cm.add(player)
            if player.big:
                player.dirty = True
            player.big = False

        # add each robot to the collision manager. If robot is big, set flag to dirty
        # and reset robot to small
        for robot in self.target.robots:
            cm.add(robot)
            if robot.big:
                robot.dirty = True
            robot.big = False

        # add projectile to collision manager
        for projectile in self.target.projectiles:
            cm.add(projectile)

        # todo castle needs a smaller collision box
        # cm.add(self.target.castle)
        # self.target.castle.big = True

        # go through all collisions for the frame
        for collision in cm.iter_all_collisions():
            # debug
            print(collision[0].coord.xy, collision[1].coord.xy)

            # check each colliding item
            for a in collision:
                other = collision[0] if collision[0] != a else collision[1]

                # if other not a projectile, set it to big and dirty
                if other not in self.target.projectiles or other.owner != self: # don't need the second condition
                                                                                # just here for completeness
                    a.big = True
                    a.dirty = True

                # if other is a projectile and the other object is not the owner of the projectile
                # remove projectile from layer and list of projectiles and stops the action
                if a in self.target.projectiles and a.owner != other:
                    self.target.remove(a)
                    self.target.projectiles.remove(a)
                    a.stop()

                    other.do(RotateBy(360, 0.5))

        cm.clear()
