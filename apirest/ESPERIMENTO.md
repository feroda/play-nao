# L'esperimento

Per tradurre queste belle parole in pratica, proviamo a definire una API REST per interagire con il robot NAO.

## Requisiti per la parte BRIDGE (ponte tra utente e NAO)

 * HTML e PHP di base (nota: nel corso non è fatto JavaScript e quindi AJAX)
 * La possibilità di PHP di trasformarsi in un client REST per interfacciarsi con la API [DAL-PHP-ALLA-API.md](DAL-PHP-ALLA-API.md)
 * La API di NAO per queste operazioni. Descritta su [API-REST-NAO.md](API-REST-NAO.md)

Quale funzionalità di NAO possiamo realizzare?

### Progetto 1 - nao-voice

Pagina web con una form HTML che include:

 - Una casella di testo con il testo da far leggere a NAO
 - Un elenco di radiobutton per la scelta della lingua

Passi per realizzarla:

 - Il web server (PHP) propone la form la sola casella di testo e il bottone per la POST
 - Il web server (PHP) recupera tramite API REST tutti i possibili linguaggi e costruisce l'elenco di radiobutton
 - Il web server (PHP) recupera tramite API REST il linguaggio attualmente impostato su NAO e lo propone selezionato all'utente

### Progetto 2 - nao-postures

Pagina web con una form HTML che include:

 - Un elenco di radiobutton per la scelta della postura

Passi per realizzarla:

 - Il web server (PHP) propone la form con il bottone per la POST
 - Il web server (PHP) recupera tramite API REST tutte le possibili posture e costruisce l'elenco di radiobutton
 - Il web server (PHP) recupera tramite API REST la postura attualmente impostata su NAO e la propone selezionata all'utente

Se vuoi procedi con la lettura (avanzata) di [IMPLEMENTARE-LA-API-REST-DI-NAO.md]()

