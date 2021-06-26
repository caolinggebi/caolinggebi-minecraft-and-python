def plantTree(x,y,z):
    mc.setBlocks(x+1,y+3,z+1,x-1,y+5,z-1,46)
    mc.setBlocks(x,y,z,x,y+4,z,46)
from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
for i in range(6):
    for j in range(6):
        for k in range(6):
            plantTree(x+i*6,y+k*7,z+j*6)
            i=i+1
            j=j+1
            k=k+1