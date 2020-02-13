# IPython log file

import urllib2

url = 'http://iismerlonimiliani.it'
urllib2.urlopen(url)
resp = urllib2.urlopen(url)
rv = resp.read()
# Trova l'indice della sottostringa <title>
ititle = rv.find('<title>')

# Trova l'indice della sottostringa </title>
iendtitle = rv.find('</title>')

# Seleziona la sottostringa che va da ititle a iendtitle
a = rv[ititle:iendtitle]

# Aumenta di 7 per togliere <title>
b = rv[ititle+7:iendtitle]

# Che cosa restituisce la seguente istruzione e perché?
c = rv[313+len('<title>')+len('I.I.S. '):411]

# Visualizza a video i risultati

print("Sottostringa da inizio <title> a fine: %s" % a)
print("Sottostringa 2: %s" % b)
print("Sottostringa 3: %s" % c)
