#!/usr/bin/python3
"""
Script generates random HTTP request logs.
"""
import random
import sys
import datetime
from time import sleep


for x in range(10000):
    err_msg = [200, 301, 400, 401, 403, 404, 405, 500]
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET {} {}\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        random.randint(1, 255),
        datetime.datetime.now(),
        '/projects/1216',
        'HTTP/1.1',
        random.choice(err_msg),
        random.randint(1, 1024)
    ))

    sys.stdout.flush()
