#WORK IN PROGRESS. AN ASTRO PI WHICH REACTS TO BLOCK HIT IN MINECRAFT

from mcpi.minecraft import Minecraft
from mcastropi import AstroPI

class MCInteractiveAstroPi:
    
    def __init__(self, pos):
        self.pos = pos
        self.mc = Minecraft.create()
        
        self.mcastropi = MCAstroPi(self.mc, self.pos)

    def _moveBy(x, y, z):
        pass
    
    def clear():
        self.mcastropi
