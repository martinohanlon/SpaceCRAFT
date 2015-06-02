from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

mc.setBlocks(-25,30,-25,
             25,30,25,
             block.STONE.id)


mc.setBlocks(-25,31,-25,
             25,40,25,
             block.AIR.id)
