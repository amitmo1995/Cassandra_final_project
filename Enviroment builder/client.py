from cassandra.cluster import Cluster
from  concurrent.futures import ThreadPoolExecutor,  wait
from datetime import date, datetime, timedelta
from decimal import *
import sys
import json


def get_keyspase(row):
    words = row.split()
    for i in range(len(words)):
        if(words[i] == "EXISTS"):
            return words[i + 1]

def execute_command(command):
    res = session.execute(command, trace=True)
    return res

# ----------create querys-------------------
path = "../Workloads/100queries60%write40%read.txt"
with open(path) as file:
    querys = [line.rstrip() for line in file]

# -----------------------Init Cassandra Connection------------------
cluster = Cluster([sys.argv[1]], port=9042)
session = cluster.connect()

session.execute(querys[0])

keyspace = get_keyspase(querys[0])

session = cluster.connect(keyspace)

session.execute(querys[1])
#-----------------------create threads------------------

traces = []
with ThreadPoolExecutor(max_workers=10) as executor:
    print("start execute_command")
    results = [executor.submit(execute_command, querys[i]) for i in range(2, len(querys))]
    wait(results)
    print('All tasks are done!')

count = 0
with open("query_trace.json", 'w') as file:
    for res in results:
        data = {
            "started_at": res.result().get_query_trace().started_at.isoformat(),
            "duration": str(res.result().get_query_trace().duration),
            "query": res.result().get_query_trace().parameters['query']
        }
        traces.append(data)
        count = count + 1
    json.dump(traces, file)
    print(count)

# with open("query_trace.json", 'r') as file:
#     traces = json.load(file)
#     for trace in traces:
#         print(trace['started_at'])
#         print(trace['duration'])
#         print(trace['query'])

cluster.shutdown()