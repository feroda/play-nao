#!/bin/bash

# Il processo hrmon ha bisogno delle librerie grafiche.
# Perciò è necessario eseguire read_hrm.py da utente "pi"
# dopo essere entrati nel raspberry con ssh -X pi@ip-del-raspberry

if [ "$DISPLAY" = "" ]; then
    echo "Per eseguire questo comando hai bisgno della variabile DISPLAY";
    echo "Hai acceduto al sistema con ssh -X pi@ip-del-raspberry?"
    exit 100;
fi

sudo chmod -R 777 /dev/shm/
cd /usr/local/play-nao/LifeIsNAO-bot/hrmon/
python read_hrm.py &
sleep 1

cat /dev/shm/hrm_instant.txt
if [ $? -eq 0 ]; then
    echo "Processo hrmon avviato correttamente";
else
    echo "Processo hrmon non avviato correttamente";
    exit 101;
fi

