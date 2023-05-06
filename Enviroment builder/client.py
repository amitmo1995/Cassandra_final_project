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
    res = session.execute_async(query, trace=True)
    result = res.result()
    trace = result.get_query_trace()
    data = {
        "started_at": trace.started_at.isoformat(),
        "duration": str(trace.duration),
        "query": trace.parameters['query']
    }
    return data

# ----------create querys-------------------
path = "../Workloads/WorkloadsForTable/100queries_rep3_insert30_update50_delete20_numOfThreads10_withTS_CLOne.txt"
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

# time.sleep(10)
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


with open("../Workloads/WorkloadsForTableRes/100queries_rep3_insert30_update50_delete20_numOfThreads10_withTS_CLOne.json", 'w') as file:
    for data in results:
        traces_res.append(data.result())
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


# # Define a function to execute the queries and log any conflicts
# def execute_queries(thread_id, queries):
#     # Connect to the Cassandra cluster
#     cluster = Cluster()
#     session = cluster.connect('amit')
    
#     # Create a batch statement
#     batch = BatchStatement()
#     for query in queries:
#         batch.add(SimpleStatement(query, consistency_level=ConsistencyLevel.ONE))
    
#     # Execute the batch statement and get the query trace
#     result = session.execute(batch, trace=True)
#     trace = result.get_query_trace()
#     print(trace)

#     # Check if any conflicts occurred
#     conflicts = []
#     for event in trace.events:
#         if event.description == 'RowWrite#CASConflict':
#             conflicts.append({
#                 'order': len(conflicts) + 1,
#                 'timestamp': event.timestamp,
#                 'description': event.description
#             })
    
#     # Write the conflict logs to a JSON file
#     with open(f'conflicts_thread{thread_id}.json', 'w') as f:
#         json.dump(conflicts, f, indent=4)
    
#     # Close the session and cluster connections
#     session.shutdown()
#     cluster.shutdown()


# path = "../Workloads/100queries_rep3_insert40_update40_delete20_numOfThreads100_withoutTS.txt"
# with open(path) as file:
#     querys = [line.rstrip() for line in file]    

# cluster = Cluster(['localhost'], port=9042, protocol_version=3)

# session = cluster.connect()

# session.execute(querys[0])

# keyspace = get_keyspase(querys[0])

# session = cluster.connect(keyspace)

# session.execute(querys[1])

# time.sleep(10)

# session.shutdown()
# cluster.shutdown()

# time.sleep(10)

# # Create 100 threads to execute the queries in parallel
# threads = []
# for i in range(2):
#     t = threading.Thread(target=execute_queries, args=(i, querys[2:]))
#     threads.append(t)
#     t.start()

# # Wait for all threads to complete
# for t in threads:
#     t.join()
