import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.util as util
from time import time, sleep

def setManyBlocks(mc, blocks):
    mc.conn.drain()
    s = ""
    for block in blocks:
        args = minecraft.intFloor(block)
        s += "world.setBlock(%s)\n"%(util.flatten_parameters_to_string(args))
    mc.conn.lastSent = s
    mc.conn.socket.sendall(s.encode())

mc = minecraft.Minecraft.create()

starttime = time()
blocksToSet = []
for x in range(0,25):
    for y in range(25,50):
        for z in range(0,25):
            blocksToSet.append((x,y,z,block.DIAMOND_BLOCK.id))
endtime = time()
print(endtime - starttime)

setManyBlocks(mc, blocksToSet)

sleep(5)

starttime = time()
for x in range(0,25):
    for y in range(25,50):
        for z in range(0,25):
            mc.setBlock(x,y,z,block.DIRT.id)
endtime = time()
print(endtime - starttime)

            

