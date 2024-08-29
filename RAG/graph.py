import streamlit as st

# tag::graph[]
from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph(
    url="neo4j://sindit_neo4j_kg",
    username="neo4j",
    password="sindit-neo4j",
)
#end::graph[]