virtualenv -p python3 .venv
. .venv/*/activate

pip install -r requirements.txt
pip install cassandra-driver --no-binary :all:


deactivate