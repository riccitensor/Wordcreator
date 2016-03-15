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
CREATE (w1:Word { value:'human',     fork:0, author_name:'admin', author_id:1, material:'', width:'', height:'', depth:'', color:'', speed:'', quantity:'', time_create:timestamp() })
CREATE (w2:Word { value:'black-man', fork:0, author_name:'admin', author_id:1, material:'', width:'', height:'', depth:'', color:'', speed:'', quantity:'', time_create:timestamp() })
CREATE (w1)-[:IS]->(w0)
CREATE (w2)-[:IS]->(w1)
"""

gdb.query(q=q)

