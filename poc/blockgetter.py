from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block

def subtractPos(pos1, pos2):
    pos = Vec3(pos1.x - pos2.x,
               pos1.y - pos2.y,
               pos1.z - pos2.z)
    return pos

mc = Minecraft.create()
noOfPos = 0

gotMiddle = False

while(not gotMiddle):
    blockHits = mc.events.pollBlockHits()
    for blockHit in blockHits:
        middlePos = blockHit.pos
        gotMiddle = True

print("Middle set = {}".format(middlePos))

while(True):
    blockHits = mc.events.pollBlockHits()
    for blockHit in blockHits:
        noOfPos += 1
        if noOfPos == 1:
            firstPos = subtractPos(blockHit.pos, middlePos)
        elif noOfPos == 2:
            secondPos = subtractPos(blockHit.pos, middlePos)
            noOfPos = 0
            blockType = mc.getBlockWithData(blockHit.pos)
            
            func = "mc.setBlocks({}, {}, {}, {}, {}, {}, {}".format(firstPos.x,
                                                                   firstPos.y,
                                                                   firstPos.z,
                                                                   secondPos.x,
                                                                   secondPos.y,
                                                                   secondPos.z,
                                                                   blockType.id)
            if blockType.data != 0:
                func += ", " + str(blockType.data) 
            
            func += ")"
            print(func)
                
                                                                    

