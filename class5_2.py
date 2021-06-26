from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
while True:
    try:
        block=int(input("What is ID number?"))
        break
    except:
        print("ERROR")
mc.setBlock(x,y,z,block)