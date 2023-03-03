# ./run arg (if docker ot non) (keyspace name) (Strategy) (replication_factor)
# ./run.sh docker barakk SimpleStrategy 1

if [ $1 == 'docker' ]
then
    docker compose up -d
    ip="localhost"
else
    apt update
    ip=${hostname -I}
    query="CREATE KEYSPACE IF NOT EXISTS $1 WITH REPLICATION = { 'class' : $2, 'replication_factor' : $3 }; exit"
    echo $query | /bin/cqlsh $ip
fi    

virtualenv -p python3 .venv
. .venv/*/activate

pip install -r requirements.txt
pip install cassandra-driver --no-binary :all:

#arg ip num_threads
python client.py $ip 1

if [ $1 == 'docker' ]
then
    docker compose down
fi    

docker volume rm $(docker volume ls -q)
deactivate