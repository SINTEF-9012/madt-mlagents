// Create person nodes
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/persons.csv' AS row
MERGE (p:Person {name: row.name, id: row.person_tmdbId});

// Create movie nodes
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/movies.csv' AS row
MERGE (m:Movie {id: row.movieId, title: row.title, plot: row.plot});


// Create relationships
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/acted_in.csv' AS row
MATCH (p:Person {id: row.person_tmdbId})
MATCH (m:Movie {id: row.movieId})
MERGE (p)-[r:ACTED_IN {role: row.role}]->(m);