#!/usr/bin/env python

import max30100
import time
import os

mx30 = max30100.MAX30100()

if not os.path.exists("/var/lib/nao-debian/"):
    os.mkdir("/var/lib/nao-debian")

while True:
    mx30.read_sensor()
    print("ir=%s red=%s" % (mx30.ir, mx30.red))
    if mx30.ir >= 1000:
        with open("/var/lib/nao-debian/dev/shm/hrm_instant.txt", "w") as f:
            f.write(str(mx30.ir))
        with open("/var/lib/nao-debian/dev/shm/hrm_buffer.txt", "w") as f:
            f.write("\n".join(map(str, mx30.buffer_ir[:-20])))
    else:
        with open("/var/lib/nao-debian/dev/shm/hrm_instant.txt", "w") as f:
            f.write("0")

    time.sleep(0.5)
