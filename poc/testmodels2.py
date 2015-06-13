#testing models in MinecraftShapes and different ways of creating hthem
from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftShape, ShapeBlock
from time import sleep

mc = Minecraft.create()

pos = mc.player.getTilePos()
pos2 = mc.player.getTilePos()
pos2.y = pos2.y + 2

print("create shape 1")
#s1 = MinecraftShape(mc, pos, [ShapeBlock(0,0,0,1)])
s1 = MinecraftShape(mc, pos)
s1.setBlock(0,0,0,1)
print(s1.shapeBlocks)

sleep(5)

print("create shape 2")
#s2 = MinecraftShape(mc, pos2, [ShapeBlock(0,0,0,2)])
s2 = MinecraftShape(mc, pos2)
s2.setBlock(0,0,0,2)
print(s2.shapeBlocks)

sleep(5)

print("clear shape 1")
s1.clear()

sleep(5)

print("clear shape 2")
s2.clear()


