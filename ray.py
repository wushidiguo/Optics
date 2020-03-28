import os
import sys
import numpy as np 

class Point:
    '''
    Creat a space point.
    '''
    __slots__ = ("x", "y", "z")
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class Ray:
    def __init__(self, point):
        pass

    @property
    def wavelength(self):
        return self._wavelenth

    @wavelength.setter
    def wavelength(self, value):
        self._wavelenth = value

    @property
    def hertz(self):
        '''
        hertz = light_speed / wavelength
        '''
        return 299792458e9 / self._wavelenth

    