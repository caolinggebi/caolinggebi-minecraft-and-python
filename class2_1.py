from mcpi.minecraft import Minecraft as mcs
import time
mc=mcs.create()
x,y,z = mc.player.getTilePos()
mc.player.setTilePos(100,100,100)
time.sleep(5)
mc.player.setTilePos(x+200,y+5000,z+500)