# About the project
This project's goal is to generate cypher queries that would then be used in a database.
The technologies that will be used are: `autogen`, `ollama`, `docker` and `python`.

The main goal of the project is to have a system with two agents:
* Coder; generates queries and will explain the results in a natural language (English)
* Executor; runs the queries and return the result to the coder 

# Starting the project
## Commands
To start a demo of the project you will need docker service running:
```bash
sudo systemctl start docker
```

To start the neo4j database you can launch the first command.
If you want to run ollama with llama3.1 too, you can do so with the second command:
```bash
sudo docker-compose up
sudo docker-compose --profile local up
```
You need to launch this in the root directory of the project where `docker-compose.yml` is.


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

You can launch the notebooks after the start of all the components.

## Important stuff 

* If you have a computer that cannot run a llm model on a GPU you can try to run it with the CPU instead. Look in the docker-compose.yml to remove this part.
If you want to use GPU instead you will need to load the correct drivers. You can find more details on the [official docker documentation](https://hub.docker.com/r/ollama/ollama).
If you want to serve a different model you can do it by changing the name of the model in the llm's healtcheck in the docker-compose.
Remember to add your token/key if you are using a non local model.

* It is possible to install requirements.txt with `poetry`, you can do that with 
```bash
poetry install $(cat requirements.txt) && \
poetry env use python
```

* You have to restart the notebook's kernel in order to make a new import effective. If it is not done it can generate an ImportError on the module you are attempting to import.

# Project's structure
In the project you will find:
* tool_agent; implements an example on how to add tool usage to an agent
* simple_agent; implements an agent that should be able to generate cypher without other information than  his previous knowledge
* retrieve_agent; implements an agent that can use some pdf files to retrieve information
* code_executor_chat; implements a chat with a coder that can use his knowledge and some files to generate a cypher query that then is executed by the executor agent
* neo4j_tools.py; contains all the tools that operates on the neo4j database
* CypherExecutor.py; implements a custom code executor to run cypher queries


# Project's state of the art 
We have a code_generator_chat notebook that implements the type of conversation explained in `About the project` part.
We will test if there is an improvement from a simple agent (has a good prompt and previous knowledge) to an agent that can be feed with manuals and other type of files to retrieve more information.
For now both of them can generate cypher queries.

The problems encountered with code-executor conversation are:
- if coder does not use a proper markdown format or if it does not separate two different queries an error will be trhown.
- if coder does not have the schema of the database, the query will probably fail because of some relation/node's name that does not exist
- if the rules for termination are given in the general rules (in the prompt), the coder will answer with the query, explains result but terminate without passing it to the executor

A future improvement should be to generate the schema with an automation and not with the call of the function.
Neo4j will be used as a database but in the future could be supported every type of graph query language.