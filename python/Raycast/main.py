from numpy import arange, radians
from math import tan, sin, cos
world = [["0"] * 10] * 10


class Vector2:
    x:int
    y:int

    def __init__(self, ix:int = 0, iy:int = 0):
        self.x = ix
        self.y = iy


class Player:
    x: int
    y: int

    def __init__(self, v2:Vector2 = Vector2(0, 0)):
        self.x = v2.x
        self.y = v2.y
    
    def shoot_ray(self, max_distance:int, angle:int):
        SQRT_TWO:float = 1.4
        # Sqrt 2 * max_distance = sqrt of a^2 + b^2 of a right angle triangle
        #  where and b are equal
        for x in arange (0.1,  SQRT_TWO*max_distance, 0.1):
            y:float = tan(radians(angle)) * x
            print(f"y: {y} || x: {x}")

    def cast_rays(self, fov:int, max_distance:int, angle:int):
        for i in arange(-fov/2, fov/2, 0.5):
            self.shoot_ray(max_distance, angle)
    

            



player = Player()
player.cast_rays(90,100, 1)

# Each tile is 100 x 100 units


