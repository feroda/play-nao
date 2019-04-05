# Lettore di frequenza cardiaca - hrmon

Richiede: matplotlib e le librerie grafiche.

Legge la frequenza cardiaca dal sensore MAX30100 e scrive i dati:

* `/var/lib/nao-debian/dev/shm/hrm_instant.txt`: per la lettura istantanea;
* `/var/lib/nao-debian/dev/shm/hrm_buffer.txt`: per le ultime 100 letture;
* `/var/lib/nao-debian/dev/shm/grafico.png`: per il grafico delle ultime 10 acquisizioni.

Questo processo è stato evoluto per creare sempre il grafico delle ultime 10 acquisizioni.

Tale funzionalità richiede l'installazione di matplotlib e anche delle librerie grafiche,
altrimenti non si riuscirebbe a produrre il png.

Per questo l'installazione deve avvenire da pacchetto quindi:

`sudo apt install python-matplotlib`
