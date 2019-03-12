# Play with NAO!

Questo progetto contiene esperimenti con il [robot NAO](https://www.ald.softbankrobotics.com).

Un elenco completo di esempi per le varie funzioni di libreria è consultabile
nella documentazione online della API di NAO all'indirizzo:
http://doc.aldebaran.com/2-1/naoqi/

## Contenuto della directory

Ecco una presentazione dei file contenuti in questo repository:

* **myfirstwords.py**: NAO parla grazie alla libreria text2speech
* **setvolume.py**: NAO si abbassa il volume

## Come riprodurre

Per riprodurre gli esperimenti è sufficiente installare:

* l'interprete python versione 2.7 (verificabile con il comando `python --version`)
* la libreria python distribuita da Aldebaraan `pynaoqi`, scarcabile dopo essersi registrati nella community di NAO

Come scritto nelle istruzioni la libreria pynaoqi deve essere installata nelle librerie di sistema,
oppure deve essere esportata la variabile di ambiente `PYTHONPATH`.
Nella shell Bash di GNU/Linux questo si può fare con il comando:

  export PYTHONPATH=/la/mia/directory/pynaoqi-2.1.2

NOTA: io ho avuto problemi con la versione  2.1.4 perciò ho installato la versione 2.1.2.
Il mio ambiente di test è una distribuzione ArchLinux

## Ringraziamenti

Questi esperimenti sono stati possibili grazie alla disponibilità del robot NAO
presso l'[Istituto di Istruzione Superiore Merloni-Miliani di Fabriano (AN)](http://www.iismerlonimiliani.it).
