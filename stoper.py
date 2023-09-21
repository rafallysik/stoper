# -*- coding: utf-8 -*-
"""
Author RL.
"""
import time
i=1 #seconds  all-the-time  indicator
minutes,seconds=(0,0)
while True:
    time.sleep(1)
    minutes=int(i/60)
    seconds=i-minutes*60 #only rest
    print("Just passed {} mins {} seconds".format(minutes,seconds))
    i+=1