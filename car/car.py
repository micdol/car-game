import pymunk as p
import pygame as g
import numpy as np
import pymunk.pygame_util

class Car:
    def __init__(self) -> None:
        self.body: p.Body = None
        self.shape: p.Body = None
        self.max_speed = 100.0
        self._debug = True

    def accelerate(self, value: float) -> None:
        '''use to make car move forward'''
        pass

    def brake(self) -> None:
        '''use to make car stop moving forward'''
        pass

    def turn(self, value: float) -> None:
        '''use to make car turn left (negative value) or right (positive value)'''
        pass

    # physics
    def update(self, physics: p.Space) -> None:
        pass

    # graphics
    def draw(self, graphics: g.Surface) -> None:
        if self._debug:
            self._draw_debug_stats(graphics)
            self._draw_debug_gizmos(graphics)

    def _draw_debug_stats(self, graphics: g.Surface) -> None:
        """draws text with position, velocity and angular velocity in top left corner"""
        font = g.font.SysFont("monospace", 16)

        if self.body is not None:
            pos = f"[{self.body.position.x:>7,.2f}, {self.body.position.y:>7,.2f}]"
            vel = f"[{self.body.velocity.x:>7,.2f}, {self.body.velocity.y:>7,.2f}] {self.body.velocity.length:.2f}"
            ang = f"[{self.body.rotation_vector.x:>7,.2f}, {self.body.rotation_vector.y:>7,.2f}] {self.body.angular_velocity:.2f}"
        text = [f"Pos: {pos}", f"Vel: {vel}", f"Ang: {ang}"]

        y = 5
        for line_text in text:
            text = font.render(line_text, 1, g.Color("black"))
            graphics.blit(text, (5, y))
            y += 16

    def _draw_debug_gizmos(self, graphics: g.Surface) -> None:
        """draws text with position, velocity and angular velocity in top left corner"""
        start = self.body.position
        end = start + self.body.velocity.normalized() * 50
        g.draw.line(graphics, g.Color("red"), start, end, 2)

        end = start + p.Vec2d(50, 0).rotated(self.body.angle)
        g.draw.line(graphics, g.Color("blue"), start, end, 2)