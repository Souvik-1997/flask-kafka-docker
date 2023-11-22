kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic shipping_data

kafka-topics.sh --list --zookeeper zookeeper:2181



kafka-console-producer.sh --topic shipping_data --zookeeper zookeeper:2181

sudo systemctl status docker

sudo systemctl start docker

sudo systemctl restart docker


sudo usermod -aG docker $USER

ls -l /var/run/docker.sock

sudo systemctl restart docker

export DOCKER_HOST=unix:///var/run/docker.sock


# start docker in background mode
docker-compose up -d

# start docker in interactive mode
docker exec -it kafka /bin/sh



kafka-console-producer.sh --topic shipping_data --bootstrap-server localhost:9092


# Inside the container with Kafka command line tools
kafka-console-consumer.sh --topic shipping_data --bootstrap-server localhost:9092 --from-beginning



# --------------------------------------------------------- #
docker-compose build

docker-compose up -d

docker-compose up --build
# --------------------------------------------------------- #

# deploy_kafka_docker
Deploy Kafka on Docker. Play with it using Python.


# Start the docker-compose with console log output
docker-compose up

# Run it in detach mode
docker-compose up -d

# Stop Everything
docker-compose down

Python
Create a virtualenv and install the requirements file

pip install -r requirements.txt

# Run consumer
python consumer.py

# Run producer
python producer.py
