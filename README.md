# About the project
This project wants to use knowledge graphs as a tool for a llm agent.
The technologies that will use are: `autogen`, `ollama`, `docker` and `python`.
Neo4j will be used as a database but in the future will be supported every type of graph database.

# Starting the project
To start a demo for the project you will need docker service running:
```bash
sudo systemctl start docker
```

To start the docker network you will have to run:
```bash
sudo docker-compose up
```

To run the python notebooks and files you firstly need to:
* Create a virtual environment 
```bash
python -m venv .venv && \
source .venv/bin/activate
```
* install the dependencies 
```bash 
pip install -r requirements.txt
```

You can try to run all the cells of wiki_tool.ipynb after starting all the components.


**Important**: If you have a computer that cannot run a llm model  as llama3.1 on a GPU you can try to run it with the CPU instead.
Look in the docker-compose.yml for further instructions on this topic.
**Important**: It is possible to install requirements.txt with `poetry`, you can do that with 
```bash
poetry install $(cat requirements.txt) && \
poetry env use python
```