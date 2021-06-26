from mcpi.minecraft import Minecraft as mcs
import time
mc=mcs.create()
x,y,z = mc.player.getTilePos()
i = 0
while True:
    time.sleep(0.1)
    y=y+10
    mc.player.setTilePos(x,y,z)
    i=i+1