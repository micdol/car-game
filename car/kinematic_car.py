import pymunk as p
import pygame as g
import numpy as np
import pymunk.pygame_util
from car import Car


class KinematicCar(Car):
    def __init__(self, physics: p.Space) -> None:
        super().__init__()
        self.img = g.transform.scale_by(
            g.image.load("F:/Code/car-game/car.png"), factor=0.5
        )
        self.body = p.Body(body_type=p.Body.KINEMATIC)
        self.body.velocity_func = self._velocity_update
        self.shape = p.Poly.create_box(body=self.body, size=self.img.get_size())
        physics.add(self.body, self.shape)

        self.max_speed = 200

    def accelerate(self, value: float) -> None:
        self.body.velocity = p.Vec2d(self.max_speed, 0).rotated(self.body.angle)

    def brake(self) -> None:
        self.body.velocity = p.Vec2d.zero()

    def turn(self, radians: float) -> None:
        # hacks to disable 0 turning radius
        # the slower car is the slower it turns, below 20 it does not turn at all
        if self.body.velocity.length > 20:
            self.body.angle += radians * (self.body.velocity.length / self.max_speed)

    def draw(self, graphics: g.Surface) -> None:
        super().draw(graphics)
        img = g.transform.rotate(self.img, np.rad2deg(-self.body.angle))
        pos = self.body.position - img.get_rect().center
        graphics.blit(img, pos)

    @staticmethod
    def _velocity_update(
        body: p.Body, gravity: p.Vec2d, damping: float, dt: float
    ) -> None:
        """dampens the velocity"""
        v, l = body.velocity.normalized_and_length()
        body.velocity = v * l * 0.9
