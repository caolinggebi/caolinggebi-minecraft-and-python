# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:53:42 2021

@author: MAO
"""
from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
print(x,y,z)
mc.setBlock(x,y,z,46)