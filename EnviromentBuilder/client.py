from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel
from concurrent.futures import ThreadPoolExecutor, wait
from cassandra.auth import PlainTextAuthProvider
from decimal import *
import json
import sys
import os

traces_res = []
consistency = {
    'ONE': ConsistencyLevel.ONE,
    'ANY': ConsistencyLevel.ANY,
    'TWO':ConsistencyLevel.TWO,
    'THREE':ConsistencyLevel.THREE,
    'QUORUM':ConsistencyLevel.QUORUM,
    'ALL': ConsistencyLevel.ALL
}


def execute_command(command, session):
    consistency_level = consistency[sys.argv[3]]
    query = SimpleStatement(command, consistency_level=consistency_level)
    res = session.execute_async(query, trace=True)
    try:
        print("-----------------------------------------------------------")
        trace = res.result().get_query_trace(max_wait_sec=1)
        data = {
            "started_at": trace.started_at.isoformat(),
            "duration": str(trace.duration),
            "query": trace.parameters['query']
        }
        print(data)
        for event in trace.events:
            print("#################")
            print(event)
            # data['events'].append(event.description)
            # print("Node: {}".format(event.source))
            # print("Source elapsed time: {} microseconds".format(event.source_elapsed))
        traces_res.append(data)
    except Exception as e:
        print("Error retrieving query trace:", e)
    return res


def get_keyspase(row):
    words = row.split()
    for i in range(len(words)):
        if(words[i] == "EXISTS"):
            return words[i + 1]


def create_session(querys):
    contact_points = os.environ.get('IPS', '').split()
    print("contact_points", contact_points)
    # Set the authentication credentials
    auth_provider = None
    if len(sys.argv) > 5:
        username = sys.argv[5]
        password = sys.argv[6]
        # 'jAE8C3B#y9P3'
        auth_provider = PlainTextAuthProvider(username=username, password=password)

    cluster = Cluster(contact_points=contact_points, auth_provider=auth_provider, protocol_version=3)
    session = cluster.connect()
    session_id = session.session_id
    print("session_id: ", session_id)
    session.execute(querys[0])
    keyspace = get_keyspase(querys[0])

    session = cluster.connect(keyspace)
    session_id = session.session_id
    session.execute(querys[1])
    return (cluster, session)


def save_table(path=None, session=None):
    res_path = path.split('.')[0] + "_res.txt"
    print("Save table to path: " + res_path)
    res = session.execute('SELECT * FROM amit.barak;')
    # Open the file in write mode
    with open(res_path, 'w') as file:
        # Iterate over the rows in the result set
        for row in res:
            print(row)
            file.write(str(row) + '\n')


if __name__ == "__main__":
    path = sys.argv[2]
    with open(path) as file:
        querys = [line.rstrip() for line in file]

    # -----------------------Init Cassandra Connection------------------
    (cluster, session) = create_session(querys)

    #-----------------------create threads------------------
    num_of_thread = int(sys.argv[4])
    with ThreadPoolExecutor(max_workers=num_of_thread) as executor:
        print("start execute_command")
        results = [executor.submit(execute_command, querys[i], session) for i in range(2, len(querys))]
        wait(results)
        print('All tasks are done!')


    save_table(path=path, session=session)

    session.execute('DROP TABLE amit.barak;')
    session.execute('DROP KEYSPACE amit;')
    session.shutdown()
    cluster.shutdown()