from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        print(block)
        mc.spawnEntity(x,y,z,63)