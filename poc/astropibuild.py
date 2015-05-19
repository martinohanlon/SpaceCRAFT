from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.setBlocks(-15, -4, -15, 15, 10, 15, 0)

#boards
mc.setBlocks(-6, -3, -9, 7, -3, 11, 35, 13)
mc.setBlocks(-6, 0, -9, 7, 0, 6, 35, 13)
#pillars
mc.setBlocks(-6, -2, -9, -6, -1, -9, 42)
mc.setBlocks(7, -2, -9, 7, -1, -9, 42)
mc.setBlocks(-6, -2, 6, -6, -1, 6, 42)
mc.setBlocks(7, -2, 6, 7, -1, 6, 42)
#gpio headers
mc.setBlocks(7, 1, -8, 7, 1, 5, 35, 15)
mc.setBlocks(7, -2, -8, 7, -1, 5, 35, 15)
#usb and ethernet port
mc.setBlocks(4, -2, 8, 6, 0, 11, 42)
mc.setBlocks(0, -2, 8, 2, 0, 11, 42)
mc.setBlocks(-5, -2, 8, -2, 0, 11, 42)
#display, power, hdmi, composite ports
mc.setBlocks(2, -2, -9, -1, -2, -9, 35, 15)
mc.setBlocks(-6, -2, -7, -6, -2, -6, 42)
mc.setBlocks(-6, -2, -2, -6, -2, 0, 42)
mc.setBlock(-6, -2, 3, 35, 15)
#led grid
mc.setBlocks(-3, 1, -8, 4, 1, -1, 155, 1)
#other astro pi components
mc.setBlocks(3, 1, 1, 4, 1, 2, 35, 15)
mc.setBlocks(3, 1, 4, 4, 1, 5, 35, 15)
mc.setBlocks(0, 1, 1, 0, 1, 2, 35, 15)
mc.setBlock(1, 1, 5, 35, 15)
mc.setBlock(-1, 1, 5, 35, 15)
mc.setBlock(-2, 1, 3, 35, 15)
mc.setBlocks(-6, 1, -5, -5, 1, -4, 35, 15)
#astropi joystick
mc.setBlock(-5, 1, 4, 42)
mc.setBlock(-4, 1, 5, 42)
mc.setBlock(-5, 1, 6, 42)
mc.setBlock(-6, 1, 5, 42)
mc.setBlock(-5, 2, 5, 35, 15)
#astro pi gaps
mc.setBlocks(-1, 0, -9, 2, 0, -9, 0)
mc.setBlocks(-5, 0, 1, -2, 0, 1, 0)
