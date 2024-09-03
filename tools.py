from neo4j import GraphDatabase as gd

# Try to connect to neo4j database (movies database is already loaded)
d = gd.driver("bolt://localhost:7687" , auth=None)
d.verify_connectivity()

def get_movie_plot(movie_title: str)->str:
    """
    This simple function will find the plot of the corresponding movie queried.

    Args:
        movie_title (str): This string is the movie's name, it must be in the database.

    Returns:
        plot (str): This string is the plot of the movie. If the movie is not in the database it will return null.
    """

    plot = d.execute_query("match (m:Movie{title: $title}) return m.plot", title=movie_title, database_="neo4j" ).records
    return plot

def plot_searcher(word: str)->list:
    """
    This simple function will find all the movies with certain keywords in their plot.

    Args:
        word (str): This string is a keyword or a group of keyword to find in a movie's plot. 

    Returns:
        title (list): The title is a list of all the movies containing the word in their plot. If the word cannot be found this will be null.
    """

    title = d.execute_query("match (m:Movie) where m.plot contains $word return m.title", word=word, database_="neo4j").records
    return title