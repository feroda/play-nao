#!/usr/bin/python

import urllib2
import json
import pprint


url = 'http://iismerlonimiliani.it'
# urllib2.urlopen(url)
# resp = urllib2.urlopen(url)



c = '''
[
        {
            "id":1,
            "author":"Indirizzo Carta presso I.I.S. Merloni Miliani", 
            "city":"Fabriano", 
            "kind":"Carta vergata"
        }
]
'''

info = json.loads(c)

answer = raw_input("quale info vuoi? ")

pprint.pprint(info)


print(info[0][answer])



