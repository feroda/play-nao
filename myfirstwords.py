from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", '192.168.1.12', 9559)
tts.say("Hello, world!")
tts.say("Grazie Davide e Lorenzo per avermi presentato, un saluto dal prof Ferroni!")
