from mcpi.minecraft import Minecraft
from mcmodels import Rocket
from time import sleep

if __name__ == "__main__":

    mc = Minecraft.create()

    rocketPos = mc.player.getTilePos()
    rocketPos.x += 5
    rocketPos.y = mc.getHeight(rocketPos.x, rocketPos.z) - 1
    
    rocket = Rocket(mc, rocketPos)
    sleep(5)
    
    try:
        #count down to blast off
        for count in range(3, 0, -1):
            mc.postToChat(str(count))
            sleep(1)
        mc.postToChat("Blast Off")

        #launch the rocket
        for up in range(rocketPos.y, 70):
            rocket.moveBy(0, 1, 0)
            sleep(0.1)
                        
    finally:
        rocket.clear()
        
