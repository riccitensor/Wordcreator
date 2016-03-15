from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

gdb = GraphDatabase("http://localhost:7474/db/data/")


if (len(sys.argv)>1):
    aid = str(sys.argv[1]) #author_id
else:
    aid = "0"

q = """MATCH ()<-[:IS]-(n) WHERE (n.visible=1 or n.visible="1") RETURN {id: id(n), value: n.value, time_create: n.time_create, author_name: n.author_name}"""

result = gdb.query(q=q)


licznik = 0;
for temp in result:
  licznik=licznik+1
  node = temp[0]


  if node['time_create'] is None:
    time_create = 0
  else:
    time_create = node['time_create']

  if node['author_name'] is None:
    author_name = "unknow"
  else:
    author_name = node['author_name']




  if (licznik>1): 
     print(',')
  print('{')
  print('"time_create":"'+str(time_create)+'",')
  print('"author_name":"'+str(author_name)+'",')
  print('"value":"'+node['value']+'",')
  print('"id":"'+str(node['id'])+'"')
  print("}")

