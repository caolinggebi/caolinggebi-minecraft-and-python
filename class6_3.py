from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
import time 
import random
while True:
    x,y,z=mc.player.getPos()
    x=x+random.uniform(-20,20)
    z=z+random.uniform(-20,20)
    mc.spawnEntity(x,y,z,99)
    time.sleep(100)