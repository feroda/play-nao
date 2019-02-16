#!/usr/bin/qemu-i386-static /usr/bin/python

import sys
import argparse

from naoqi import ALProxy

NAO_IP = '192.168.10.10'

def go_to_posture(args):

    postureProxy = ALProxy("ALRobotPosture", args.ip, args.port)
    postureProxy.goToPosture(args.posture, 0.5)

def say(args):

    ttsProxy = ALProxy("ALTextToSpeech", args.ip, args.port)
    ttsProxy.say(args.dialog)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default=NAO_IP)
    parser.add_argument('--port', default=9559)
    parser.add_argument('--posture', default="Crouch")
    parser.add_argument('--dialog', default="Ciao a tutti!")
    args = parser.parse_args()
    go_to_posture(args)
    say(args)
