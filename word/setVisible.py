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

if (len(sys.argv)>2):
    visible = str(sys.argv[2])
else:
    visible = "0"



gdb = GraphDatabase("http://localhost:7474/db/data/")


q = """MATCH (n)
WHERE ID(n)="""+filtr+"""
SET n.visible = '"""+visible+"""'"""

gdb.query(q=q)