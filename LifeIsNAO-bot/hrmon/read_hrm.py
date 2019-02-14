#!/usr/bin/env python

import max30100
import time

mx30 = max30100.MAX30100()

while True:
    mx30.read_sensor()
    print("ir=%s red=%s" % (mx30.ir, mx30.red))
    time.sleep(0.5)
