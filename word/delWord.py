from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

def isset(variable):
	return variable in locals() or variable in globals()

if (len(sys.argv)>1):
    filtr = str(sys.argv[1])
else:
    filtr = ""

gdb = GraphDatabase("http://localhost:7474/db/data/")

q = """MATCH p=(h:Word)-[rs:HAS*]-(x) WHERE id(h) = """+filtr+"""
    WITH p, x, EXTRACT(x IN NODES(p)| x.value) AS nodes
    FOREACH (n IN rels(p)| 
         DELETE n)
    DELETE x
    RETURN nodes"""

gdb.query(q=q)