from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
width=9
height=9
lenght=9
block=12
air=0
mc.setBlocks(x,y,z,x+width,y+height,z+lenght,block)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+lenght-1,air)
