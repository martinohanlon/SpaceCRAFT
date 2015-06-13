#utility to help making big builds, if you it 2 blocks, it fills the gap in between
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
pos = mc.player.getPos()
mc.player.setPos(pos.x, pos.y +5, pos.x)
noOfPos = 0

while True:
    blockHits = mc.events.pollBlockHits()
    for blockHit in blockHits:
        noOfPos += 1
        if noOfPos == 1:
            firstPos = blockHit.pos
        elif noOfPos == 2:
            secondPos = blockHit.pos
            noOfPos = 0
            blockType = mc.getBlockWithData(blockHit.pos)
            #if its a book case, use AIR instead
            if blockType.id == 47:
                blockType = block.Block(0)
            mc.setBlocks(firstPos, secondPos, blockType.id, blockType.data)

