# ./run arg (if docker ot non) (keyspace name) (Strategy) (replication_factor)
# ./run.sh docker barakk SimpleStrategy 1

if [ $1 == 'docker' ]
then
    docker run --name cassandra1 -d -v "$(pwd)/data:/var/lib/cassandra" -p 9042:9042 --network cassandra -d cassandra
    sleep 2
    docker run --name cassandra2 -d --network cassandra -e CASSANDRA_SEEDS=cassandra1 cassandra
    sleep 2
    docker run --name cassandra3 -d --network cassandra -e CASSANDRA_SEEDS="cassandra1 , cassandra2"   cassandra
    sleep 2
    echo "all dockers runs"
    docker exec cassandra1 cqlsh -e "CREATE KEYSPACE IF NOT EXISTS $2 WITH REPLICATION = { 'class' : '$3', 'replication_factor' : '$4' }; exit"

else
    apt update
    ip=${hostname -I}
    query="CREATE KEYSPACE IF NOT EXISTS $1 WITH REPLICATION = { 'class' : $2, 'replication_factor' : $3 }; exit"
    echo $query | /bin/cqlsh $ip
fi    

docker ps