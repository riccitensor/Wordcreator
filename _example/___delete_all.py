from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """MATCH n OPTIONAL MATCH (n)-[r]-() DELETE n, r;"""

gdb.query(q=q)

