#-*- coding: utf-8 -*-

from naoqi import ALProxy
import time

NAO_IP = '192.168.10.10'
NAO_PORT = 9559

x = 1
y = 1
motionProxy = ALProxy("ALMotion", NAO_IP, NAO_PORT)
motionProxy.stopMove()

# leftArmEnable  = True
# rightArmEnable  = True
# motionProxy.setWalkArmsEnabled(leftArmEnable, rightArmEnable
#
# # motionProxy.moveInit()
# #
# # motionProxy.move(x, y, 0)
# # motionProxy.stopMove(x, y, 0)
