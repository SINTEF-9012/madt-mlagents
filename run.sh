#!/bin/bash

#pip install -r requirements.txt
sudo docker-compose up &
yarn run dev &

cd connection
python minio_api.py & 
python neo4j_api.py & 
python analytics_api.py & 
python influxdb_api.py &