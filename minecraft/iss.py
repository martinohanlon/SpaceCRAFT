from minecraftstuff import MinecraftShape
from minecraftstuff import ShapeBlock
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block
from time import sleep

class ISS():
    def __init__(self, pos):

        self.pos = pos
        #self.mc = Minecraft.create("192.168.1.103")
        self.mc = Minecraft.create()

        #create the ISS shape
        self.issShape = MinecraftShape(self.mc, self.pos, visible = False)

        #create the ISS using setBlock(s) commands
        # an arrow
        self.issShape.setBlocks(0, 0, -5, 0, 0, 5, block.WOOL.id, 1)
        self.issShape.setBlocks(1, 0, 4, 1, 0, 4, block.WOOL.id, 2)
        self.issShape.setBlocks(-1, 0, 4, -1, 0, 4, block.WOOL.id, 2)
        self.issShape.setBlocks(2, 0, 3, 2, 0, 3, block.WOOL.id, 3)
        self.issShape.setBlocks(-2, 0, 3, -2, 0, 3, block.WOOL.id, 3)
        self.issShape.setBlocks(3, 0, 2, 3, 0, 2, block.WOOL.id, 4)
        self.issShape.setBlocks(-3, 0, 2, -3, 0, 2, block.WOOL.id, 4)
        
        #make the iss visible
        self.issShape.draw()
    
    def rotate(self, yaw, pitch, roll):
        self.issShape.rotate(yaw, pitch, roll)

    def clear(self):
        self.issShape.clear()

#test
if __name__ == "__main__":

    pos = Vec3(0, 20, 0)

    iss = ISS(pos)
    try:
        sleep(5)
        iss.rotate(140.588146932, 1.77246589269, 0.195452679949)
        sleep(5)
        #iss.rotate(0, 0, 0)
        #sleep(5)
        #iss.rotate(0, 90, 0)
        #sleep(5)
        #iss.rotate(0, 0, 0)
        #sleep(5)
        #iss.rotate(0, 0, 90)
        #sleep(5)
        #iss.rotate(0, 0, 0)
        #sleep(5)
    finally:
        iss.clear()
