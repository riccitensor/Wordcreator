from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

def isset(variable):
	return variable in locals() or variable in globals()

if (len(sys.argv)>1):
    nodeid = str(sys.argv[1])
else:
    nodeid = ""



gdb = GraphDatabase("http://localhost:7474/db/data/")



q = """MATCH (w:Word) WHERE id(w)="""+nodeid+""" return {id:id(w),value:w.value,author_id:w.author_id};"""

result = gdb.query(q=q)


for temp in result: 
  node = temp[0]
  print(node['author_id'])
