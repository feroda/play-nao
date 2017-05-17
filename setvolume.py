# -*- coding: utf-8 -*-

import sys
from naoqi import ALProxy

def main(robotIp, volume):

    tts = ALProxy("ALTextToSpeech", robotIp, 9559)
    tts.say("Ciao quinto B, mi abbasso il volume")
    tts.setVolume(volume)
    tts.say("Ora il volume è al {}%% scusate il disturbo per prima!".format(volume*100))


if __name__ == "__main__":
    robotIp = "127.0.0.1"
    volume = 0.2

    if len(sys.argv) > 1:
        robotIp = sys.argv[1]
        if len(sys.argv) == 3:
            try:
                volume = float(sys.argv[2])
            except TypeError:
                print('Volume deve essere espresso in forma decimale tra 0 e 1 con separatore "."')
    else:
        print "Usage python almotion_rest.py <robotIP> <volume percent float 0-1> (optional default: 127.0.0.1 0.2)"

    main(robotIp, volume)
