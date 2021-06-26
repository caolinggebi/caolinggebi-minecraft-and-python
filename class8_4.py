def plantTree(x,y,z):
    mc.setBlocks(x+1,y+3,z+1,x-1,y+5,z-1,46)
    mc.setBlocks(x,y,z,x,y+2,z,46)
from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
for i in range(5):
    for j in range(5):
        for k in range(5):
            plantTree(x+i*i,y+k*k,z+j*j)
            i=i+1
            j=j+1
            k=k+1
            
