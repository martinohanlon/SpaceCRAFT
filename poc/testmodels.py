from mcmodels import Rocket, Arrow
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

pos = mc.player.getTilePos()
pos2 = pos.clone()
pos2.y + 10

print("create rocket")
r = Rocket(mc, pos)

sleep(5)

print("create rocket")
a = Arrow(mc, pos2)

sleep(5)

print("clear arrow")
a.clear()

sleep(5)

print("clear rocket")
r.clear()


