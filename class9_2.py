from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
number=1
for i in range(number):
    mc.spawnEntity(x,y,z,99)
    mc.postToChat(str(i+1)+"隻鐵巨人")