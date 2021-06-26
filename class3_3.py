# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:16:45 2021

@author: MAO
"""

from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
print(x,y,z)
mc.setBlocks(x+100,y,z+100,x-100,y,z-100,7)
mc.setBlock(x,y,z,0)