// Create person nodes
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/persons.csv' AS row
MERGE (p:Person {name: row.name, tmdbId: row.person_tmdbId});

// Create movie nodes
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/movies.csv' AS row
MERGE (m:Movie {movieId: row.movieId, title: row.title});


// Create relationships
LOAD CSV WITH HEADERS FROM 'https://data.neo4j.com/importing-cypher/acted_in.csv' AS row
MATCH (p:Person {tmdbId: row.person_tmdbId})
MATCH (m:Movie {movieId: row.movieId})
MERGE (p)-[r:ACTED_IN {role: row.role}]->(m);


// Use pre-created embeddings
LOAD CSV WITH HEADERS
FROM 'https://data.neo4j.com/llm-fundamentals/openai-embeddings.csv'
AS row
MATCH (m:Movie) where apoc.node.id(m) = toInteger(row.movieId)
CALL db.create.setNodeVectorProperty(m, 'plotEmbedding', apoc.convert.fromJsonList(row.embedding))
RETURN count(*)


// Create vector indexes
CREATE VECTOR INDEX `moviePlots` IF NOT EXISTS
FOR (m:Movie)
ON m.plotEmbedding
OPTIONS {indexConfig: {
 `vector.dimensions`: 1536,
 `vector.similarity_function`: 'cosine'
}}
