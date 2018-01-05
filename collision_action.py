from cocos.actions import Action, RotateBy

import config
from game_config import game_board
from cocos.euclid import Vector3, Vector2
from cocos.collision_model import CircleShape, CollisionManagerGrid

# todo create a collision action which game layer will do and collect all the collidables and then
# todo do them in step method of collision action

class CollisionAction(Action):
    def init(self):
        width, height = game_board["size"]
        self.collision_manager = CollisionManagerGrid(0, width, 0, height, width // 10, height // 10)

    def start(self):
        self.step(0)

    def step(self, dt):
        cm = self.collision_manager

        for player in self.target.players:
            cm.add(player)
            if player.big:
                player.dirty = True
            player.big = False

        for robot in self.target.robots:
            cm.add(robot)
            if robot.big:
                robot.dirty = True
            robot.big = False

        for fruit in self.target.projectiles:
            cm.add(fruit)

        #todo castle needs a smaller collision box
        #cm.add(self.target.castle)
        #self.target.castle.big = True

        for collision in cm.iter_all_collisions():
            print(collision[0].coord.xy, collision[1].coord.xy)
            for a in collision:
                other = collision[0] if collision[0] != a else collision[1]
                if other not in self.target.projectiles or other.owner != self:
                    a.big = True
                    a.dirty = True
                if a in self.target.projectiles and a.owner != other:
                    self.target.remove(a)
                    self.target.projectiles.remove(a)

                    other.do(RotateBy(360, 0.5))

        cm.clear()
