# ./run arg (if docker ot non) (keyspace name) (Strategy) (replication_factor)
# ./run.sh docker barakk SimpleStrategy 1

#if run with dockers -- ./run.sh docker <path to generator file> <consistencyLevel> <numOfThread>

#if with the cluster -- ./run.sh <path to generator file> <consistencyLevel> <numOfThread>

# if run with azrieli cluster the ips '['62.90.89.27', '62.90.89.28', '62.90.89.29', '62.90.89.39']'
# if with docker '['localhost']'

#!/bin/bash

virtualenv -p python3 .venv
. .venv/*/activate

pip install -r requirements.txt

if [ $1 == 'docker' ]
then
    docker compose up -d
    ips=('localhost')
    sleep 60
    export IPS="${ips[@]}"
    python client.py $ips $2 $3 $4
    docker compose down
    docker volume rm $(docker volume ls -q)
else
    ips=('62.90.89.27')
    export IPS="${ips[@]}"
    python client.py $ips $1 $2 $3
fi
 
deactivate
