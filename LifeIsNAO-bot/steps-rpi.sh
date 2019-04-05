#!/bin/bash

# FIXME: questo non funziona, perché il processo hrmon
# ha bisogno delle librerie grafiche. Perciò è necessario
# eseguire read_hrm.py da utente pi@ dopo essere entrati nel raspberry
# con ssh -X pi@ip-del-raspberry

# APPUNTI da testare
# chmod -R 777 /var/lib/nao-debian/dev/shm/
# cd /usr/local/play-nao/LifeIsNAO-bot/hrmon/
# python read_hrm.py &
echo "ERROR: non ti funzionera' il grafico se lo lanci da root. bisogna implementare il FIXME qui sopra"
exit 100
systemctl restart hrmon

cat /var/lib/nao-debian/dev/shm/hrm_instant.txt

cd /var/lib/nao-debian/usr/local/play-nao
git pull

for d in sys dev proc run; do
	mount -o bind /$d /var/lib/nao-debian/$d
done
mount -o bind /dev/pts /var/lib/nao-debian/dev/pts

chroot /var/lib/nao-debian/

umount /var/lib/nao-debian/dev/pts
for d in sys dev proc run; do
	umount /var/lib/nao-debian/$d
done
