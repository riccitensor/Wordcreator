from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """
CREATE (wr:Word { value : 'Root' })
CREATE (w0:Word { value : 'Object' })
CREATE (w0)-[:IS]->(wr)


"""

gdb.query(q=q)

