#!/usr/bin/env python

import json
import copy

from bottle import route, run, template
from bottle import post, get, request, put, response

from naoapiqi import ALProxy

NAO_IP = '127.0.0.1'
NAO_PORT = 9559

# porte TCP per il bind
BIND_IP = '0.0.0.0'
BIND_PORT = 8080

# Modello risposta JSON come documentato su
# https://github.com/feroda/play-nao/blob/master/apirest/API-REST-NAO.md
FEROJSON = {
    "status": "OK",
    "code": 200,
    "notices": [],
    "meta": {},
    "body": {}
}

@route('/api/v1/languages/')
def naoapi_languages():
    langs = ['French', 'Chinese', 'English', 'German', 'Italian', 'Japanese', 'Korean', 'Portuguese', 'Spanish']
    rv = copy.copy(FEROJSON)
    rv["body"] = {"languages": langs}
    # Se restituisco un dizionario, Bottle.py manda una risposta json
    # (gestisce Content-Type ed encoding!)
    return rv

@put('/api/v1/languages/<lang>')
def naoapi_set_language(lang):

    rv = copy.copy(FEROJSON)

    # TODO: verifica che sia un linguaggio valido con API NAO, ma fai cache
    langs = ['French', 'Chinese', 'English', 'German', 'Italian', 'Japanese', 'Korean', 'Portuguese', 'Spanish']
    if lang in langs:
        data = json.load(request.body)
        if data["active"] is True:
            print("imposto la lingua attiva a %s" % lang)
            nao_set_language(lang)
    else:
        rv["code"] = 404
        rv["notices"] = ["Language %s is not available" % lang]
        response.status = 404

    # Se restituisco un dizionario, Bottle.py manda una risposta json
    # (gestisce Content-Type ed encoding!)
    return rv

@post('/api/v1/text2speech/')
def naoapi_text2speech():

    rv = copy.copy(FEROJSON)
    data = json.load(request.body)

    actions = ['say']
    if data.get("action") in actions:
        text = data.get("text", "nulla")
        print("NAO dira' %s" % text)
        nao_speak(text)
    else:
        rv["code"] = 400
        rv["notices"] = ["Request not good for this API, needed keys 'action' and 'text'"]
        response.status = 400

    # Se restituisco un dizionario, Bottle.py manda una risposta json
    # (gestisce Content-Type ed encoding!)
    return rv


# -- fero NAO mini lib!

tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
def nao_speak(msg):
    tts.say(msg)

def nao_get_languages():
    return tts.getAvailableLanguages()

def nao_set_language(lang):
    tts.setLanguage(lang)


run(host=BIND_IP, port=BIND_PORT)
