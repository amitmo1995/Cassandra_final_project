from cassandra.cluster import Cluster
import sys
from decimal import *
import threading
import time
import os
import concurrent.futures
import threading
import queue


#-----------------------Init Cassandra Connection------------------
cluster = Cluster([sys.argv[1]])
session = cluster.connect('barak')
session.execute( "CREATE TABLE IF NOT EXISTS barak.Barak (userid text PRIMARY KEY, name text, age int, last_update_timestamp timestamp)")

#-------------

def execute_command(command, num_t):
    print("command => ", command, "Num => ", num_t)
    session.execute(command)
    return num_t


# ----------create querys-------------------  
path = os.path.dirname(__file__) + "/100queries60%write40%read.txt"
print(path)
with open(path) as file:
    querys = [line.rstrip() for line in file]

#-----------------------create threads------------------

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(execute_command, querys[i], i) for i in range(len(querys))]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
