#-*- coding: utf-8 -*-

from naoqi import ALProxy
import time

NAO_IP = '192.168.10.11'
NAO_PORT = 9559

x = 1
y = 1
motionProxy = ALProxy("ALMotion", NAO_IP, NAO_PORT)
motionProxy.stopMove()

