from cassandra.cluster import Cluster
from cassandra.query import dict_factory, QueryTrace, SimpleStatement
from cassandra import ConsistencyLevel
from cassandra.auth import PlainTextAuthProvider
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

    query = SimpleStatement(command, consistency_level=ConsistencyLevel.ONE)
    # id = uuid.uuid4()
    # trace = QueryTrace(id, query)
    res = session.execute(query, trace=True)
    return res

# ----------create querys-------------------
path = "../Workloads/10queries_rep3_insert3_update5_delete2_numOfThreads10_withTS.txt"
with open(path) as file:
    querys = [line.rstrip() for line in file]

# -----------------------Init Cassandra Connection------------------
cluster = Cluster([sys.argv[1]], port=9042, protocol_version=3)
# cluster = Cluster(['62.90.89.27'], port=9042, protocol_version=3)

session = cluster.connect()

session.execute(querys[0])

keyspace = get_keyspase(querys[0])

session = cluster.connect(keyspace)

session.execute(querys[1])
#-----------------------create threads------------------

# statement = SimpleStatement(querys[1], fetch_size=10)
# r = session.execute_async(statement)
# print(r.result().get_query_trace())

traces_res = []
with ThreadPoolExecutor(max_workers=10) as executor:
    print("start execute_command")
    results = [executor.submit(execute_command, querys[i]) for i in range(2, len(querys))]
    wait(results)
    print('All tasks are done!')

with open("traces_res/10queries_rep3_insert3_update5_delete2_numOfThreads10_withTS.json", 'w') as file:
    for result in results:
        trace = result.result().get_query_trace()
        data = {
            "started_at": trace.started_at.isoformat(),
            "duration": str(trace.duration),
            "query": trace.parameters['query']
        }
        traces_res.append(data)
    json.dump(traces_res, file)


# get trace with query
# count = 0
# res = session.execute('SELECT * FROM system_traces.sessions;')
# for row in res:
#     count = count + 1
#     print(row)

session.execute('DROP TABLE amit.barak;')
session.execute('DROP KEYSPACE amit;')

# with open("query_trace.json", 'r') as file:
#     traces = json.load(file)
#     for trace in traces:
#         print(trace['started_at'])
#         print(trace['duration'])
#         print(trace['query'])

session.shutdown()
cluster.shutdown()