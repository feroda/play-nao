#-*- coding: utf-8 -*-

from naoqi import ALProxy
import time

NAO_IP = '192.168.10.11'
NAO_PORT = 9559

motionProxy = ALProxy("ALMotion", NAO_IP, NAO_PORT)
postureProxy = ALProxy("ALRobotPosture", NAO_IP, NAO_PORT)
postureProxy.goToPosture("StandInit", 0.5)

x          = 0.6
y          = 0.0
theta      = 0.0
frequency  = 1.0
motionProxy.setWalkTargetVelocity(x, y, theta, frequency)

time.sleep(4.0)

motionProxy.stopMove()

