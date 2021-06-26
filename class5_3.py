from mcpi.minecraft import Minecraft as mcs
mc=mcs.create()
username=input("What is your name ?")
message=input("What is your message?")
mc.postToChat("<"+username+">"+message)