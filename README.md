# About the project
This project wants to generate cypher queries to be then used in a database.
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

You can launch all the cells of wiki_tool.ipynb after starting all the components.


**Important**: If you have a computer that cannot run a llm model as llama3.1 on a GPU you can try to run it with the CPU instead. Look in the docker-compose.yml to remove this part.
If you want to use GPU instead you will need to load the correct drivers. You can find more details on the [official docker documentation](https://hub.docker.com/r/ollama/ollama).

**Important**: It is possible to install requirements.txt with `poetry`, you can do that with 
```bash
poetry install $(cat requirements.txt) && \
poetry env use python
```

**Important**: You have to restart the notebook's kernel in order to make a new import effictive. If it is not done it can generate an ImportError on the module you are attempting to import.

# Project's structure
In the project you will find:
* wiki_tool.ipynb; small demo on how to use tools with agents
* tool_agent.ipynb; similar to wiki_tool but the tools retrieve data from a neo4j database
* simple_agent.ipynb; simple agent that generates cypher queries using his previous knowledge
* retrieve_agent.ipynb; adds a pdf file to be used by the coder to generate better queries
* feedback_agent.ipynb; similar of retrieve_agent but adds a feedback agent 
* tester_agent.ipynb; similar to feedback_agent but adds a code executor 

* tools.py; contains all the tool to connect and query the neo4j database
* CypherExecutor.py; implements a custom code executor to run cypher queries

All this notebook were made to test how to add agents in an already tested chatgroup.
They will probably be kept in a different branch to not cause confusion.

**Important**: the structure of the project can be refactored to reflect the logic of the project itself and to improve modularity/non-repetitivness

## Future modules
The project will add some more agents to the retrieve_agent chat. 
The goal is to have a system where a coder generates the cypher query and with the help of some controller agents to improve it.
The main idea is to have only two agents:
* Coder; generates cypher queries and will explain the results
* Executor; runs the cypher queries and return the result to the coder 

**Important**: some or all of this future ideas may be not implemented due to project's requirement.