import logging 
from neo4j import GraphDatabase as gd
from neo4j.exceptions import Neo4jError
from IPython.core.magic import register_line_cell_magic

def connect() -> gd.driver:
    """
    Tries to connect to a neo4j database hosted in a Docker container called 'graph'
    """
    
    try:
        driver = gd.driver("bolt://localhost:7687" , auth=None)
    except ConnectionError:
        raise ConnectionError("Something went wrong with the connection to the database!")
    else:
        driver.verify_connectivity()
        return driver

def plot_searcher(word: str, driver=None)->list:
    """
    This simple function will find all the movies with certain keywords in their plot.

    Args:
        word (str): This string is a keyword or a group of keyword to find in a movie's plot. 

    Returns:
        title (list): The title is a list of all the movies containing the word in their plot. If the word cannot be found this will be null.
    """

    if not driver: driver = connect()

    title = driver.execute_query("match (m:Movie) where m.plot contains $word return m.title", word=word, database_="neo4j").records
    return title

def run_query(query: str, driver=None)-> str:
    """
    It will run the given cypher query in a neo4j database

    Args:
        query (str): The query to perform

    Returns:
        _type_: It depends on the query result
    """
    if not driver: driver = connect()

    log   = logging.getLogger()
    res   = driver.session(database="neo4j").run(query)
    data  = res.data() # Needed before we use consume
    notif = res.consume().summary_notifications

    for n in notif:
        s = n.severity_level
        if s == "WARNING":
            log.error("%r", s.message)
        elif s == "INFORMATION":
            log.warning("%r", s.message)
        else:
            # severity == "UNKNOWN"
            log.info("%r", s.message)

    return data
    

@register_line_cell_magic
def cypher(line, cell=None):
    if not cell: res = run_query(line)
    else:  res = run_query(cell)
    return res 