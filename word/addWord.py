from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

def isset(variable):
	return variable in locals() or variable in globals()

if (len(sys.argv)>2):
    filtr = str(sys.argv[1]) #slowo zdefiniowane
    filtru = str(sys.argv[2]) #nowe slowo usera
else:
    filtr = ""
    filtru = ""

if (len(sys.argv)>3):
    author_name = str(sys.argv[3]) #author_name
else:
    author_name = ""

if (len(sys.argv)>4):
    author_id = str(sys.argv[4]) #author_id
else:
    author_id = 0


gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """Match (w:Word) WHERE id(w) = """+filtr+""" CREATE (wn:Word { value:'"""+filtru+"""',author_name:'"""+author_name+"""', author_id:'"""+str(author_id)+"""',visible: "1", time_create:timestamp()}) CREATE (wn)-[:IS]->(w) return {id: id(wn)};"""
res = gdb.query(q=q)

for temp in res: 
  node = temp[0]
  print(node['id'])
