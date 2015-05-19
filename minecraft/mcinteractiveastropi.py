from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcastropi import MCAstroPi

class MCInteractiveAstroPi:

    LED_GRID_POS = Vec3(4, 1, -8)
    
    def __init__(self, mc, pos):
        self.pos = pos
        self.mc = mc
        
        self.mcastropi = MCAstroPi(self.mc, self.pos)

    def interact(self, x, y, z):
        """
        If you pass a block position, the interactive astro pi will
        see if that block is an interactive one and take the neccessary action
        """
        #see if this block is an interactive one
        #get this blocks relative position
        shapeBlock = self.mcastropi.getShapeBlock(x, y, z)
        print(shapeBlock.originalPos)
        print(shapeBlock.tag)

    def _moveBy(self, x, y, z):
        pass
    
    def clear(self):
        self.mcastropi.clear()

    def _turnLEDPosIntoXY(self, pos):
        """
        Internal. Turns an minecraft pos into a led x,y position
        """
        

if __name__ == "__main__":

    mc = Minecraft.create()

    pos = Vec3(0,20,0)

    mcap = MCInteractiveAstroPi(mc, pos)

    try:
        while(True):
            for blockHit in mc.events.pollBlockHits():
                mcap.interact(blockHit.pos.x, blockHit.pos.y, blockHit.pos.z)

    finally:
        mcap.clear()
            
