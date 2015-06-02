from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.setBlocks(-20, -4, -20, 20, 20, 20, 0)

#main body
mc.setBlocks(-2, 0, -16, -2, 0, 16, 42)
mc.setBlocks(-1, -1, 16, -1, -1, -16, 42)
mc.setBlocks(0, -2, -16, 0, -2, 16, 42)
mc.setBlocks(1, -1, 16, 1, -1, -16, 42)
mc.setBlocks(2, 0, -16, 2, 0, 16, 42)
mc.setBlocks(1, 1, 16, 1, 1, -16, 42)
mc.setBlocks(0, 2, -16, 0, 2, 16, 42)
mc.setBlocks(-1, 1, 16, -1, 1, -16, 42)
mc.setBlocks(1, 0, -17, -1, 0, -17, 42)
mc.setBlocks(0, 1, -17, 0, -1, -17, 42)
mc.setBlocks(0, 1, 17, 0, -1, 17, 42)
mc.setBlocks(-1, 0, 17, 1, 0, 17, 42)

#across 
mc.setBlocks(-12, -1, 0, 7, -1, 0, 42)
mc.setBlocks(-12, 0, 1, 8, 0, 1, 42)
mc.setBlocks(7, 1, 0, -12, 1, 0, 42)
mc.setBlocks(-12, 0, -1, 8, 0, -1, 42)
mc.setBlock(-13, 0, 0, 42)

#bit on top of the across
mc.setBlock(-13, 0, 0, 42)
mc.setBlock(-10, 1, -1, 42)
mc.setBlock(-10, 2, 0, 42)
mc.setBlock(-10, 1, 1, 42)
mc.setBlock(-5, 1, 1, 42)
mc.setBlock(-5, 1, -1, 42)

#central spire
mc.setBlocks(-1, 2, 0, -1, 4, 0, 42)
mc.setBlocks(0, 3, -1, 0, 4, -1, 42)
mc.setBlocks(1, 2, 0, 1, 4, 0, 42)
mc.setBlocks(0, 3, 1, 0, 4, 1, 42)
mc.setBlock(0, 5, 0, 42)

#the T
mc.setBlocks(7, 1, -5, 7, 1, 4, 42)
mc.setBlocks(8, 0, 4, 8, 0, -5, 42)
mc.setBlocks(6, 0, -5, 6, 0, 4, 42)
mc.setBlocks(7, -1, 4, 7, -1, -5, 42)
mc.setBlock(7, 0, -6, 42)
mc.setBlock(7, 0, 5, 42)

#solar panel supports
mc.setBlocks(14, 0, 14, 3, 0, 14, 42)
mc.setBlocks(3, 0, 9, 14, 0, 9, 42)
mc.setBlocks(14, 0, -10, 3, 0, -10, 42)
mc.setBlocks(3, 0, -14, 14, 0, -14, 42)
mc.setBlocks(-3, 0, -14, -15, 0, -14, 42)
mc.setBlocks(-15, 0, -10, -3, 0, -10, 42)
mc.setBlocks(-3, 0, 9, -14, 0, 9, 42)
mc.setBlocks(-14, 0, 14, -3, 0, 14, 42)

#solar panels
mc.setBlocks(-4, 0, 15, -15, 0, 15, 35, 1)
mc.setBlocks(-15, 0, 13, -4, 0, 13, 35, 1)
mc.setBlocks(-4, 0, 10, -15, 0, 10, 35, 1)
mc.setBlocks(-15, 0, 8, -4, 0, 8, 35, 1)
mc.setBlocks(-4, 0, -9, -16, 0, -9, 35, 1)
mc.setBlocks(-16, 0, -11, -4, 0, -11, 35, 1)
mc.setBlocks(-4, 0, -13, -16, 0, -13, 35, 1)
mc.setBlocks(-16, 0, -15, -4, 0, -15, 35, 1)
mc.setBlocks(4, 0, -15, 15, 0, -15, 35, 1)
mc.setBlocks(15, 0, -13, 4, 0, -13, 35, 1)
mc.setBlocks(4, 0, -11, 15, 0, -11, 35, 1)
mc.setBlocks(15, 0, -9, 4, 0, -9, 35, 1)
mc.setBlocks(4, 0, 8, 15, 0, 8, 35, 1)
mc.setBlocks(15, 0, 10, 4, 0, 10, 35, 1)
mc.setBlocks(4, 0, 13, 15, 0, 13, 35, 1)
mc.setBlocks(15, 0, 15, 4, 0, 15, 35, 1)
