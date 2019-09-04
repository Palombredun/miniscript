import math
import random as rdm

from .constants import *
from .units import *


class Projectile():
    def __init__(self):
        self.v0 = 10 * SPEED
        self.alpha = 60 * DEGREE_TO_RADIAN
        self.h = 1.0 * METER
        self.m = 1.0 * KILO

    def x_t(self, t):
        return (self.v0*math.cos(self.alpha)*t)

    def y(self, t):
        return (-g*(t**2)/2 + self.v0*math.sin(self.alpha) + self.h)

    def y_x(self, x):
        #return ( (-g*x**2)/(2 * self.v0**2 * math.cos(self.alpha)**2) + \
        #    math.tan(self.alpha)*x + self.h)
        return ((-0.5 * g * x**2)/(self.v0**2 * math.cos(self.alpha)**2) + \
                x*math.tan(self.alpha) + self.h)

    def basic_throw(self, x_min: int=0, x_max: int=20) -> tuple:
        y_dx = []
        intervall_x = [0.2*i for i in range(x_min, x_max)]
        for dx in intervall_x:
            y_dx.append(self.y_x(dx))
        return (intervall_x, y_dx)

    def throw_random_angle(self, x_min: int=0, 
                                x_max: int=30, 
                                delta_alpha: int=15) -> tuple:
        y_dx = []
        intervall_x = [0.5*i for i in range(x_min, x_max)]
        self.alpha = rdm.uniform(self.alpha - delta_alpha*DEGREE_TO_RADIAN, \
                                self.alpha + delta_alpha*DEGREE_TO_RADIAN)
        for dx in intervall_x:
            y_dx.append(self.y_x(dx))
        return (intervall_x, y_dx)