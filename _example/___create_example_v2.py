from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """CREATE (w0:Obiect { value : 'Object' })
CREATE (w1:Word { value:'game' })
CREATE (w2:Word { value:'unreal' })
CREATE (w3:Word { value:'a' })
CREATE (w4:Word { value:'b'})
CREATE (w5:Word { value:'c' })
CREATE (w6:Word { value:'d'})
CREATE (w1)-[:IS]->(w0)
CREATE (w2)-[:IS]->(w1)
CREATE (w3)-[:HAS]->(w2)
CREATE (w4)-[:HAS]->(w3)
CREATE (w5)-[:HAS]->(w4)
CREATE (w6)-[:HAS]->(w5)
CREATE (w6)-[:HAS]->(w3)
"""

gdb.query(q=q)

