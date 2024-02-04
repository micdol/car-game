import pymunk as p
import pygame as g
import numpy as np
import pymunk.pygame_util
from car import *


def main() -> None:
    g.init()
    graphics = g.display.set_mode((1280, 720))

    physics = p.Space()

    # used to draw some pymunk debugging shapes, colliders etc
    debug_options = p.pygame_util.DrawOptions(graphics)
    debug_options.shape_kinematic_color = (255, 0, 0)

    car = KinematicCar(physics)
    car.body.position = (720, 360)

    fps = 60.0
    clock = g.time.Clock()
    is_running = True
    while is_running:
        # input
        events = g.event.get()
        keys = g.key.get_pressed()
        if any([e.type == g.QUIT for e in events]) or keys[g.K_ESCAPE]:
            is_running = False

        if keys[g.K_UP] or keys[g.K_w]:
            car.accelerate(10)
        elif keys[g.K_DOWN] or keys[g.K_s]:
            car.brake()

        if keys[g.K_LEFT] or keys[g.K_a]:
            car.turn(-0.1)
        elif keys[g.K_RIGHT] or keys[g.K_d]:
            car.turn(0.1)

        # physics update
        physics.step(1 / fps)

        # graphics
        graphics.fill(g.Color("white"))
        car.draw(graphics)
        physics.debug_draw(debug_options)

        g.display.flip()

        clock.tick(fps)


if __name__ == "__main__":
    main()
