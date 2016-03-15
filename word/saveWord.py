from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

def isset(variable):
	return variable in locals() or variable in globals()

if (len(sys.argv)>1):
    query = str(sys.argv[1])
else:
    query = ""

gdb = GraphDatabase("http://localhost:7474/db/data/")
gdb.query(q=query)