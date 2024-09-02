from neo4j import GraphDatabase as gd

d = gd.driver("bolt://localhost:7687" , auth=None)
d.verify_connectivity()

def get_movie_plot(movie_title: str)->str:
    plot = d.execute_query("match (m:Movie{title: $title}) return m.plot", title=movie_title, database_="neo4j" ).records
    return plot

def plot_searcher(word: str)->str:
    title = d.execute_query("match (m:Movie) where m.plot contains $word return m.title", word=word, database_="neo4j").records
    return title


