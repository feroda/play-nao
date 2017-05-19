#!/usr/bin/env python
"""
Dimostrazione minimale che fa parlare il robot NAO
tramite una GET HTTP sul PATH /speak/<testo che NAO deve leggere>
effettuata all'IP di NAO sulla porta 8080
"""

from bottle import run, get, template
from naoqi import ALProxy

# IP e porta per il bind del web server (ascolto del socket TCP)
BIND_IP = '0.0.0.0'
BIND_PORT = 8080

# IP e PORTA su cui e' contattabile NAO
# Se il web server gira su NAO lasciare queste impostazioni
# (anche in questo caso si apre un socket TCP, ma
# verso il servizio TCP offerto da NAO)
NAO_IP = '127.0.0.1'
NAO_PORT = 9559

@get('/speak/<msg>')
def nao_speak_with_get_on_the_specific_path(msg):
    """
    Fa pronunciare a NAO un messaggio e restituisce un estratto di HTML
    """
    tts.say(msg)
    return template('<b>NAO ha detto</b>: "{{msg}}"', msg=msg)

# Quando eseguo lo script python inizializzo il modulo text2speech di NAO
# lo metto globale al web server visto che lo userei in piu' di una funzione della API
tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)

# ed eseguo il web server Bottlepy
# che sara' raggiungibile sull'IP specificato
# (oppure qualunque IP della macchina se 0.0.0.0)
# e sulla porta specificata
run(host=BIND_IP, port=BIND_PORT)
