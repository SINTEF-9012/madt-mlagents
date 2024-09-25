// Create constraint
CREATE CONSTRAINT movieId IF NOT EXISTS FOR (m:Movie) REQUIRE m.id IS UNIQUE;
CREATE CONSTRAINT personId IF NOT EXISTS FOR (p:Person) REQUIRE p.id IS UNIQUE;

// Create person nodes
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/persons.csv' AS row
MERGE (p:Person {name: row.name, tmdbId: row.person_tmdbId});

// Create movie nodes
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/movies.csv' AS row
MERGE (m:Movie {movieId: row.movieId, title: row.title, plot: row.plot});


// Create more nodes and relationships
CALL apoc.example.movies;