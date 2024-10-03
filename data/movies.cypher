// Create constraint
CREATE CONSTRAINT IF NOT EXISTS FOR (m:Movie) REQUIRE m.ID IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (p:Person) REQUIRE p.ID IS UNIQUE;

// Create person nodes
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/persons.csv' AS row
CREATE (p:Person {name: row.name, ID: row.person_tmdbId, bio: row.bio, born: row.born, bornIn: row.bornIn});

// Create movie nodes
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/movies.csv' AS row
CREATE (m:Movie {ID: row.movieId, title: row.title, plot: row.plot, genres: row.genres, rating: row.imdbRating});

// Create relationships
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/acted_in.csv' AS row
MATCH (p:Person {ID: (row.person_tmdbId)})
MATCH (m:Movie {ID: (row.movieId)})
MERGE (p)-[r:ACTED_IN]->(m)
SET r.role = row.role;

LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/directed.csv' AS row
MATCH (p:Person {ID: (row.person_tmdbId)})
MATCH (m:Movie {ID: (row.movieId)})
MERGE (p)-[r:DIRECTED]->(m);