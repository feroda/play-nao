from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", '192.168.10.10', 9559)

print(tts.getAvailableLanguages())
# tts.setLanguage('Italian')
tts.say("mani in alto")
