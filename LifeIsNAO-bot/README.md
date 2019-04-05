# LifeIsNAO-bot

Bot Telegram di interazione con NAO

Installare python-telegram-bot
Installare il binding python di naoqi (da scaricare dal sito di Aldebaran vedere info su README.md del repository [play-nao](https://github.com/feroda/play-nao/)

Esportare nella variable di ambiente PYTHONPATH il percorso della libreria naoqi:

  export PYTHONPATH=/opt/pynaoqi-python2.7-2.1.2.17-linux64/

Impostare TOKEN, NAO_IP e NAO_PORT nel `settings.py`

Eseguire il bot

  python hellonao.py

a scopo di debug si può eseguire il comando specificando ip e porta del servizio NAOQI

  python hellonao.py --ip <NAO IP> --port <NAOQI PORT, default 9559>


## Cosa fa questo bot

Questo bot Telegram sarà utilizzato per la NAO Challenge.
Verrà installato su un Raspberry collegato a NAO via WiFi.

### Prova A: presentazione del team

Il comando `/naopresent` farà apparire in chat una tastiera
dove ogni bottone scriverà in chat il comando `/p <nome del giocatore>`.

Il comando `/p` consentirà NAO di chiamare ad uno ad uno i partecipanti del team.
Il partecipante chiamato dirà il proprio ruolo.

### Prova B: NAO per l'inclusione sociale sul tema del (cyber)bullismo

NAO è un punto d'ascolto che chiede un nick al ragazzo che va a parlarci.
Il testo registrato del ragazzo viene salvato in memoria nelle chiavi Domanda/N
(dove N = intero da 1 al numero massimo di domande).

Dopo aver salvato in memoria la risposta, NAO lancia l'evento "AnswerGiven".

Il programma in ascolto dell'evento (in esecuzione sul Raspberry) lo intercetta,
consulta le chiavi di memoria di NAO relative alle domande ed invia **in un unico messaggio**:

  * il nick
  * le domande
  * le risposte
  * la lettura delle ultime 10 frequenze cardiache (HRM)

nella CHAT ESPERTI.

#### La lettura delle ultime 10 frequenze cardiache

Mentre il ragazzo risponde alle domande di NAO deve tenere il dito su un sensore di frequenza cardiaca collegato al Raspberry.

Sulla scheda è in esecuzione un processo che legge il sensore e scrive le letture in 2 files:

  * `/var/lib/nao-debian/dev/shm/hrm_instant.txt`: per la lettura istantanea;
  * `/var/lib/nao-debian/dev/shm/hrm_buffer.txt`: per le ultime 100 letture.
  * `/var/lib/nao-debian/dev/shm/grafico.png`: per il grafico delle ultime 10 letture

Quando il bot riceve l'evento può inviare l'ultima lettura
traendola da `hrm_instant.txt` e le ultime 10 letture traendole dall'altro file.

#### Plus

(TODO)

Gli esperti chiedono tramite comando `/naosay` altre informazioni che vengono
riportate nella chat esperti. Come si fa questa cosa?

Il bot riceve il testo delle domande e le mette in memoria, poi solleva un evento "newQuestion"

In Choregraphe un programma è in ascolto di "newQuestion" e con il blocco "Say"
viene chiesta la domanda. La risposta verrà messa in "Domanda/100"
e verrà lanciato l'evento "AnswerGiven" come sopra.



