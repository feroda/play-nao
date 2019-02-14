#!/usr/bin/env python

import sys
from naoqi import ALProxy

NAO_IP = '127.0.0.1'
NAO_PORT = 9000

try:
	posture = sys.argv[1]
except IndexError:
	posture = "Crouch"

postureProxy = ALProxy("ALRobotPosture", NAO_IP, NAO_PORT)
postureProxy.goToPosture(posture, 0.5)
