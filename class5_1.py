from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
block=int(input("What is ID number?"))
#block=int(block)
#mc.setBlock(x,y,z,int(block))
mc.setBlock(x,y,z,block)