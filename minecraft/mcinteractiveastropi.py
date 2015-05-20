"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcinteractiveastropi.py

An interactive astro pi board created in Minecraft which responds when
hit (right clicked) with a sword
"""
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block
from mcastropi import MCAstroPi
from astro_pi import AstroPi
from time import sleep

class MCInteractiveAstroPi:
    """
    An interactive AstroPi in minecraft. Pass block positions to the .interact
    method and it will tell you whats there or make it work.
    """
    #the position of the top left of the LED grid
    LED_GRID_POS = Vec3(4, 1, -8)

    #WOOL colours to led colours
    LED_WOOL_COL = {0: [255, 255, 255],
                    1: [255, 128, 0],
                    2: [204, 0, 204],
                    3: [102, 178, 255],
                    4: [255, 255, 0],
                    5: [0, 255, 0],
                    6: [255, 204, 204],
                    7: [96, 96, 96],
                    8: [192, 192, 192],
                    9: [0, 204, 204],
                    10: [76, 0, 153],
                    11: [0, 0, 255],
                    12: [102, 51, 0],
                    13: [0, 153, 0],
                    14: [255, 0, 0],
                    15: [0, 0, 0]}
    
    
    def __init__(self, mc, ap, pos):
        #store variables
        self.pos = pos
        self.mc = mc
        self.ap = ap

        #set the joystick to move the astro pi horizontally
        self.joy_horizontal = True

        #create the minecraft astro pi shape
        self.mcastropi = MCAstroPi(self.mc, self.pos)

        self.mc.postToChat("SpaceCRAFT - interactive Astro Pi")
        self.mc.postToChat("Hit (right click) the Astro Pi with a sword to see what it does")

    def interact(self, pos):
        """
        If you pass a block position, the interactive astro pi will
        see if that block is an interactive one and take the neccessary action
        """
        #see if this block is an interactive one
        #get this blocks relative position
        shapeBlock = self.mcastropi.getShapeBlock(pos.x, pos.y, pos.z)
        if shapeBlock != None:
            #led grid
            if shapeBlock.tag == "led":
                #work out what colour to go to next
                nextWoolColour = shapeBlock.blockData + 1
                if nextWoolColour == 16: nextWoolColour = 0
                ledColour = self.LED_WOOL_COL[nextWoolColour]
                
                #find out where the led is
                ledX, ledY = self._turnLEDPosIntoXY(shapeBlock.originalPos)
                ap.set_pixel(ledX, ledY, ledColour)
                
                #change the colour of the block
                # this is the 'right' way to do it but its slow because it works out
                # all the potential changes before only changing 1 block
                #self.mcastropi.setBlock(shapeBlock.originalPos.x,
                #                        shapeBlock.originalPos.y,
                #                        shapeBlock.originalPos.z,
                #                        shapeBlock.blockType,
                #                        nextWoolColour,
                #                        shapeBlock.tag)
                
                shapeBlock.blockData = nextWoolColour
                mc.setBlock(pos.x, pos.y, pos.z, block.WOOL.id, nextWoolColour)
                
            elif shapeBlock.tag == "rpi_board":
                mc.postToChat("This is the Raspberry Pi computer")
                
            elif shapeBlock.tag == "astropi_board":
                mc.postToChat("This is the Astro Pi SENSE HAT, it can read")
                mc.postToChat(" lots of information about the world")
                
            elif shapeBlock.tag == "rpi_gpio":
                mc.postToChat("The Raspberry Pi's GPIO header, it talks to")
                mc.postToChat(" the Astro Pi through these pins")

            elif shapeBlock.tag == "astropi_gpio":
                mc.postToChat("The Astro Pi SENSE HAT GPIO header, it talks to")
                mc.postToChat(" the Rasberry Pi through these pins")

            elif shapeBlock.tag == "processor":
                mc.postToChat("This is the Raspberry Pi's CPU")
                
            elif shapeBlock.tag == "usb":
                mc.postToChat("USB ports where peripherals such as a keyboard")
                mc.postToChat(" and mouse can be connected.")
                
            elif shapeBlock.tag == "ethernet":
                mc.postToChat("An ethernet port which can be used to connect")
                mc.postToChat(" to the internet")

            elif shapeBlock.tag == "camera":
                mc.postToChat("A port where a camera can be connected to take")
                mc.postToChat(" pictures and video")
            
            elif shapeBlock.tag == "display":
                mc.postToChat("A port where a display can be connected")
                
            elif shapeBlock.tag == "power":
                mc.postToChat("Micro usb connector where you plug a power supply")
                mc.postToChat(" into the Raspberry Pi")
                
            elif shapeBlock.tag == "hdmi":
                mc.postToChat("HDMI port for connecting the Raspberry Pi to a")
                mc.postToChat(" TV or monitor")
                
            elif shapeBlock.tag == "composite":
                mc.postToChat("A composite video and audio connector, most used")
                mc.postToChat(" for plugging in headphones")
                
            elif shapeBlock.tag == "level_shifter":
                mc.postToChat("Astro Pi's Logic Level Shifter it allows electronics")
                mc.postToChat(" with different voltages to work together")
                
            elif shapeBlock.tag == "atmel":
                mc.postToChat("Astro Pi's Atmel Tiny micro controller which monitors")
                mc.postToChat(" the joystick and controls the led driver")
                
            elif shapeBlock.tag == "orientation":
                mc.postToChat("Astro Pi's Accelerometer, Magnetometer & Gyroscope")
                mc.postToChat(" which gets its orientation")
                orientation = self.ap.get_orientation()
                mc.postToChat(" yaw = {}, pitch = {}, roll = {}".format(round(orientation["yaw"],2), round(orientation["pitch"],2), round(orientation["roll"],2)))
                
            elif shapeBlock.tag == "humidity":
                mc.postToChat("Astro Pi's Humidity and Temperature Sensor")
                humidity = self.ap.get_humidity()
                temp = self.ap.get_temperature_from_humidity()
                mc.postToChat(" humidity = {}, temperature = {}".format(round(humidity,2), round(temp, 2)))
                
            elif shapeBlock.tag == "pressure":
                mc.postToChat("Astro Pi's Pressure and Temperature Sensor")
                pressure = self.ap.get_pressure()
                temp = self.ap.get_temperature_from_pressure()
                mc.postToChat(" pressure = {}, temperature = {}".format(round(pressure,2), round(temp, 2)))
                
            elif shapeBlock.tag == "eeprom":
                mc.postToChat("Astro Pi's ID EEPROM, this tells the Raspberry Pi what")
                mc.postToChat(" is attached")
                
            elif shapeBlock.tag == "led_driver":
                mc.postToChat("Astro Pi's LED driver which controls the LED matrix")
                
            elif shapeBlock.tag == "joy_up":
                self.joyUp()                              

            elif shapeBlock.tag == "joy_down":
                self.joyDown()

            elif shapeBlock.tag == "joy_left":
                self.joyLeft()

            elif shapeBlock.tag == "joy_right":
                self.joyRight()
                
            elif shapeBlock.tag == "joy_button":
                self.joyButton()
                
    def _turnLEDPosIntoXY(self, pos):
        """
        Internal. Turns a pos on the minecraft astro pi into a led x,y position
        on the real astro pi
        """
        y = (pos.x - self.LED_GRID_POS.x) * -1
        x = pos.z - self.LED_GRID_POS.z
        return x, y

    def joyButton(self):
        """
        Swaps the joy stick direction from horizontal to vertical or vice versa
        """
        if self.joy_horizontal:
            self.joy_horizontal = False
            mc.postToChat("Changed to vertical movement")
        else:
            self.joy_horizontal = True
            mc.postToChat("Changed to horizontal movement")
    
    def joyLeft(self):
        """
        Moves the astro Pi left or down
        """
        if self.joy_horizontal:
            self.mcastropi.moveBy(0,0,-1)
        else:
            #move down
            self.mcastropi.moveBy(0,-1,0)
    
    def joyRight(self):
        """
        Moves the astro Pi right or up
        """
        if self.joy_horizontal:
            self.mcastropi.moveBy(0,0,1)
        else:
            #move up
            self.mcastropi.moveBy(0,1,0)
    
    def joyUp(self):
        """
        Moves the astro Pi forward or up
        """
        if self.joy_horizontal:
            #move forward
            self.mcastropi.moveBy(1,0,0)
        else:
            self.mcastropi.moveBy(0,1,0)
    
    def joyDown(self):
        """
        Moves the astro Pi backward or down
        """
        if self.joy_horizontal:
            #move backward
            self.mcastropi.moveBy(-1,0,0)
        else:
            self.mcastropi.moveBy(0,-1,0)
    
    def clear(self):
        """
        Clears the mc astro pi
        """
        self.ap.clear()
        self.mcastropi.clear()

#run
if __name__ == "__main__":

    print("SpaceCRAFT - Minecraft Interactive Astro Pi")

    #create connection to minecraft
    mc = Minecraft.create()

    #create the astro pi object
    ap = AstroPi()
    #read data from the astro pi to initialise it
    ap.get_orientation()
    ap.get_humidity()
    ap.get_pressure()

    #find the players position and create the astro pi 10 blocks above them
    pos = mc.player.getTilePos()
    pos.y += 10
    mcap = MCInteractiveAstroPi(mc, ap, pos)

    try:
        print("CTRL C to quit")
        while(True):
            #each time a block is hit pass it to the interactive astro pi
            for blockHit in mc.events.pollBlockHits():
                mcap.interact(blockHit.pos)
            #keep reading the astro pi orientation data otherwise it goes out of sync
            ap.get_orientation()
            #sleep for a bit
            sleep(0.1)
            
    finally:
        #clear the interactive astro pi
        mcap.clear()
        
            
