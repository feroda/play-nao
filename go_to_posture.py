# -*- encoding: UTF-8 -*-

'''Demo problem #1'''

from naoqi import ALProxy

robotIP = '192.168.10.11'
PORT 9559

postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

postureProxy.goToPosture("Stand", 0.3)
postureProxy.goToPosture("StandInit", 0.3)


"""
Dear NAO support,
I am a python software developer, senior GNU/Linux sysadmin and teacher in the school that has bought this robot some time ago.

I am a NAO newbie. I have verified carefully the problem also with other tech teachers of the school.

We have two problems, and I don't know if they are related. They can be reproduced by moving the robot from Stand to StandInit posture.

#1. NAO loses its center of gravity, with shoulders moved forward (it would fall face down). We have never made him falling because we were nearby the robot all the times we did this posture change.

#2. NAO emits weird crunching rumors (by motors?).
This second problem occurs when the robot change position, (but seems not from Rest to Stand, so probably when it moves/rotates its back, in example when it does its greeting with Coreographe)

I have written some python code with the naoqi library to demonstrate the problem.

from naoqi import ALProxy

robotIP = '192.168.10.11'
PORT 9559
postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
postureProxy.goToPosture("Stand", 0.3)
postureProxy.goToPosture("StandInit", 0.3)


Hope these information help to spot the bug, and that we can solve it. Thank you in advance
Luca Ferroni
'""
