from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

def isset(variable):
	return variable in locals() or variable in globals()

if (len(sys.argv)>3):
    filtru = str(sys.argv[1]) #nowe slowo usera
    author_name = str(sys.argv[2]) #author_name
    author_id = str(sys.argv[3]) #author_id
else:
    filtru = ""
    author_name = ""
    author_id = 0

gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """Match (ob:Obiect) CREATE (w:Word { value:'"""+filtru+"""',author_name:'"""+author_name+"""', author_id:'"""+str(author_id)+"""', time_create:timestamp()}) CREATE (w)-[:IS]->(ob) return {id: id(w)};"""
res = gdb.query(q=q)

for temp in res: 
  node = temp[0]
  print(node)
