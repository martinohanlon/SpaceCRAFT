from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

mc.setBlocks(72,1,120,
             120,1,72,
             block.STONE.id)


