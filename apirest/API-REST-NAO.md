# La API-REST di NAO by fero

Tutte le richieste restituiscono un JSON della forma:

```
{
   "status" : <OK o ERROR>,
   "code" : codice di stato (obbligatorio se errore),
   "notices" : [ notifiche (obbligatorio un elemento se errore a meno che il codice non sia un unico caso documentato) ],
   "meta" : { <oggetto JSON con metainformazioni> } (opzionale),
   "body" : { <oggetto JSON con gli attributi della risposta specifica> } (opzionale),
}
```

che chiameremo FEROJSON

## Lingue

###  Recupero lingue disponibili

`HTTP GET api/v1/languages/`
  * Restituisce FEROJSON.body:
    * "languages": lista dei linguaggi disponibili

Esempio:

```
GET /api/v1/languages/ HTTP/1.1
Host: nao

```

### Modifica linguaggio attivo

`HTTP PUT api/v1/languages/:language_name`
  * con JSON:
    * "active": true

Esempio:

```
PUT /api/v1/languages/Italian HTTP/1.1
Host: nao

{ "active": true }
```

## Lettura testo

### Esegui lettura testo

`HTTP POST api/v1/text2speech/`
  * con JSON:
    * "action": "say",
    * "text": testo da leggere

Esempio:

```
PUT /api/v1/text2speech/ HTTP/1.1
Host: nao

{ "action": "say", "text": "Ciao mondo!" }
```

