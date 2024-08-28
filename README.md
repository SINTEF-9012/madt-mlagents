# MADT4BC: Multi-Aspect Digital Twin for Business Continuity

## Installation
This software requires `node v20.2.0` and `yarn v1.22.19`.

To install dependencies from yarn you have to run:

```bash
yarn install
```

Make sure chart.js, react-chartjs-2 and cl-react-graph are installed as well, if not:

```bash 
yarn add chart.js react-chartjs-2 cl-react-graph
```

### Environment creation
Create an environment and install Python (v3.10), flask (v3.0.0), minio (v7.1.17), neo4j (v5.15.0), poetry (v1.7.1), openai (v0.28.1), pyyaml (v6.0.1), strenum (v0.4.15), dpkt (v1.9.8), influxdb-client (v1.42.0) and paho-mqtt (v1.6.1).
You can install the dependencies using:
*  connection/environment.yml file to create Conda environment:
```bash
conda env create -f environment.yml
conda env list # verify install
```
* requirements.txt with pip or poetry, the example with pip is:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Setup
To run all the environments you have to:
* Launch databases, llms,... with docker-compose

```bash
sudo docker-compose up
```
* run the neodash environment
```bash
yarn run dev
```
* navigate to the connection folder and run the 4 api.py files (make sure you have activated the virtual environment)

```bash
python minio_api.py
python neo4j_api.py
python analytics_api.py
python influxdb_api.py
```

### Accessing Database and Dashboard
All the username and password for the database access are detailed in `docker-compose.databases.yml`.

Open the minio database in browser: [http://localhost:9099](http://localhost:9099).
Create a user and set the policy to read-write. The access and secret keys need to be updated in the `connection/minio_config.ini` file, and in `statistics/minio_config.ini`.
Create a bucket and update the bucket name in `connection/minio_api.py` file. Add the PCAP file to the bucket. 

Open the neo4j database in browser: [http://localhost:7474](http://localhost:7474).
 **Create new database**: If the database is empty, you can load one by opening Neo4j. Copy the content from `samples/<latest-date-sample>.cypher` and past it into the query box of the Neo4j browser, then execute the query. 
The name/type of the PCAP file needs to correspond to the endpoint/type properties of the static node. 

Open the dashboard in browser: [http://localhost:3000](http://localhost:3000), choose "New Dashboard". 
**Create new dashboard**: Press load dashboard button in left side panel. Choose "Select from file", and choose a sample dashboard (e.g. `samples/dashboard-<latest-date>.json`).


## User Guide for NeoDash
NeoDash comes with built-in examples of dashboards and reports. For more details on the types of reports and how to customize them, see the [User Guide](https://neo4j.com/labs/neodash/2.2/user-guide/).


## Questions / Suggestions
If you have any questions about NeoDash, please reach out to the maintainers:
- Create an [Issue](https://github.com/neo4j-labs/neodash/issues/new) on GitHub for feature requests/bugs.
- Connect with us on the [Neo4j Discord](https://neo4j.com/developer/discord/).
- Create a post on the Neo4j [Community Forum](https://community.neo4j.com/).

> NeoDash is a free and open-source tool developed by the Neo4j community - not an official Neo4j product. If you have a need for a commercial agreement around training, custom extensions or other services, please contact the [Neo4j Professional Services](https://neo4j.com/professional-services/) team.
