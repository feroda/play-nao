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

papers = [
    {  "id": 1,
       "author":"Indirizzo Carta presso I.I.S. Merloni Miliani",
       "city":"Fabriano",
       "kind":"Carta vergata"
    },
    {  "id": 2,
       "author": "Autore 2",
       "city": "Fabriano",
       "kind": "Carta "
    },
    {  "id": 3,
       "author": "Autore 3",
       "city": "Fabriano",
       "kind": "Carta vergata"
    }
]

@route('/api/v1/papers/')
def paperapi_list():
    # Se restituisco un dizionario, Bottle.py manda una risposta json
    # (gestisce Content-Type ed encoding!)
    return {"body": papers}

@put('/api/v1/papers/<id>')
def paperapi_get(id):

    rv = { "body" : None }

    for paper in papers:
        if paper['id'] == id:
            rv["body"] = paper

    return rv

run(host=BIND_IP, port=BIND_PORT)
