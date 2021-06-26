from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
#mc.setBlocks(x+1,y+3,z+1,x-1,y+5,z-1,46)
#mc.setBlocks(x,y,z,x,y+4,z,2)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            mc.setBlock(x+i,y+k,z+j,46)
for i in range(3):
    mc.setBlock(x+1,y-i,z+1,46)