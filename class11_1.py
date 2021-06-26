from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
from random import randint
a=0
x,y,z=mc.player.getPos()
com=randint(0,16)
for i in range(10):
    for j in range(10):
        num=randint(0,16)
        mc.setBlock(x+i,y,z+j,35,num)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        if data==com:
            mc.postToChat("you win >-<")
            break
        elif data<com:
            mc.postToChat("you answar<com")
            a=a+1
        else:
            mc.postToChat("you answer>com")
            a=a+1
        if a==10:
            mc.postToChat("you lose\'_'/")
            break