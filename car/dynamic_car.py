import pymunk as p
import pygame as g
import numpy as np
import pymunk.pygame_util
from car import Car

# todo not working yet
class DynamicCar(Car):
    def __init__(self, physics: p.Space) -> None:
        super().__init__()
        self.img = g.transform.scale_by(
            g.image.load("F:/Code/car-game/car.png"), factor=0.5
        )
        self.body = p.Body(body_type=p.Body.DYNAMIC)
        self.shape = p.Poly.create_box(body=self.body, size=self.img.get_size())
        self.shape.mass = 1
        self.shape.friction = 1
        physics.add(self.body, self.shape)
        self.max_speed = 200

    def accelerate(self, value: float) -> None:
        # applies force
        force = p.Vec2d(50, 0).rotated(self.body.angle)
        self.body.apply_force_at_local_point(force)

    def brake(self) -> None:
        self.shape.friction
        # todo thing of somethign better
        if self.body.velocity.length > 10:
            force = p.Vec2d(-50, 0).rotated(self.body.angle)
            self.body.apply_force_at_local_point(force)
        else:
            self.body.velocity = 0

    def turn(self, value: float) -> None:
        self.body.torque = value * 100000

    def draw(self, graphics: g.Surface) -> None:
        super().draw(graphics)
        img = g.transform.rotate(self.img, np.rad2deg(-self.body.angle))
        pos = self.body.position - img.get_rect().center
        graphics.blit(img, pos)
