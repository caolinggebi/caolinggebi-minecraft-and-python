# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:38:24 2021

@author: MAO
"""
from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
print(x,y,z)
i=0
x=x+15
while i<3:
    mc.setBlock(x+i,y,z,46)
    mc.setBlock(x+i,y+1,z,152)
    i=i+1