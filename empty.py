# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:28:55 2021

@author: MAO
"""

from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+1000,y+100,z+1000,x-1000,y-100,z-1000,0)