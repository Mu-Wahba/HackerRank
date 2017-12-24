#!/bin/python3

import datetime
ft='%a %d %b %Y %H:%M:%S %z'
for _ in range(int(input())):
    t1=datetime.datetime.strptime(input(),ft)
    t2=datetime.datetime.strptime(input(),ft)
    print(int(abs(t1-t2).total_seconds()))
