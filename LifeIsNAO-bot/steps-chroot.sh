#!/bin/bash

if [ ! `id -u` -eq 0 ]; then
    echo "This script must be launched by root"
    exit 100
fi

cat /var/lib/nao-debian/dev/shm/hrm_instant.txt
if [ ! $? -eq 0 ]; then
    echo "You must launch the hrmon service with the steps-hrmon.sh script as user pi";
    exit 101;
fi

for d in sys dev proc run; do
	mount -o bind /$d /var/lib/nao-debian/$d
done
mount -o bind /dev/shm /var/lib/nao-debian/dev/shm
mount -o bind /dev/pts /var/lib/nao-debian/dev/pts

chroot /var/lib/nao-debian/

umount /var/lib/nao-debian/dev/shm
umount /var/lib/nao-debian/dev/pts
for d in sys dev proc run; do
	umount /var/lib/nao-debian/$d
done
