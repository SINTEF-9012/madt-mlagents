from neo4j import GraphDatabase as gd

def connect() -> gd.driver:
    """
    Tries to connect to a neo4j database hosted in a Docker container called 'graph'
    """
    
    #TODO: shoud add a try/except
    driver = gd.driver("bolt://localhost:7687" , auth=None)
    driver.verify_connectivity()

    return driver

#TODO: Is there a way to use run_query instead of this?
def plot_searcher(word: str, driver=None)->list:
    """
    This simple function will find all the movies with certain keywords in their plot.

    Args:
        word (str): This string is a keyword or a group of keyword to find in a movie's plot. 

    Returns:
        title (list): The title is a list of all the movies containing the word in their plot. If the word cannot be found this will be null.
    """

    if (driver is None): driver = connect()

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
    if (driver is None): driver = connect()

    #TODO: Should control if there are notifications (warning, errors,...)
    return driver.session(database="neo4j").run(query).data()
    