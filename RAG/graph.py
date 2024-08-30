import streamlit as st

# tag::graph[]
from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph(
    url="neo4j://localhost",
    username="neo4j",
    password="useruser",
)
#end::graph[]