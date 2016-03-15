from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """CREATE (w0:Obiect { value : 'Object' })
CREATE (w1:Word { value:'human',     fork:0, author_name:'admin', author_id:1, material:'', width:'', height:'', depth:'', color:'', speed:'', quantity:'', time_create:timestamp() })
CREATE (w2:Word { value:'black-man', fork:0, author_name:'admin', author_id:1, material:'', width:'', height:'', depth:'', color:'', speed:'', quantity:'', time_create:timestamp() })
CREATE (w3:Word { value:'legs',      fork:0, author_name:'admin', author_id:1, material:'', width:'', height:'', depth:'', color:'', speed:'', quantity:'2', time_create:timestamp() })
CREATE (w4:Word { value:'hands',     fork:0, author_name:'admin', author_id:1, material:'', width:'', height:'', depth:'', color:'', speed:'', quantity:'2', time_create:timestamp() })
CREATE (w5:Word { value:'biceps',    fork:0, author_name:'admin', author_id:1, material:'', width:'', height:'', depth:'', color:'', speed:'', quantity:'2', time_create:timestamp() })
CREATE (w6:Word { value:'calfs',     fork:0, author_name:'admin', author_id:1, material:'', width:'', height:'', depth:'', color:'', speed:'', quantity:'2', time_create:timestamp() })
CREATE (w1)-[:IS]->(w0)
CREATE (w2)-[:IS]->(w1)
CREATE (w3)<-[:HAS]-(w2)
CREATE (w4)<-[:HAS]-(w2)
CREATE (w5)<-[:HAS]-(w4)
CREATE (w6)<-[:HAS]-(w3)"""

gdb.query(q=q)

