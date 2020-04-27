import sys
import os
import time
import devcon_win

time.sleep(5)
t=devcon_win status "PCI\VEN_8086&DEV_9D71&SUBSYS_224717AA&REV_21"
print(t)