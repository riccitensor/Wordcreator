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
    author_id = str(sys.argv[2]) #author_id
else:
    author_id = "0"

and_author = ""
if (author_id!="0"):
    and_author = """ and w.author_id='"""+author_id+"""' """

gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """MATCH (p)<-[:IS]-(w:Word) WHERE w.visible <> "0" and lower(w.value)=~'"""+filtr+""".*' """+and_author+"""                 return {id: id(w), value: w.value, time_create:w.time_create,default:w.default, visible:w.visible, author_name:w.author_name,author_id:w.author_id, parent:p.value} """




result = gdb.query(q=q)

print("{")
licznik = 0;

for temp in result:
  licznik=licznik+1
  node = temp[0]

  if node['time_create'] is None:
    time_create = 0
  else:
    time_create = node['time_create']

  if node['author_id'] is None:
    author_id = 0
  else:
    author_id = node['author_id']


  if node['author_name'] is None:
    author_name = "unknow"
  else:
    author_name = node['author_name']

  if node['default'] is None:
    default = 0
  else:
    default = node['default']

  if node['visible'] is None:
    visible = 0
  else:
    visible = node['visible']


  if (licznik>1): 
     print(',')
  print('"'+str(licznik)+'": {')
  print('"time_create":"'+str(time_create)+'",')
  print('"author_name":"'+str(author_name)+'",')
  print('"author_id":"'+str(author_id)+'",')
  print('"default":"'+str(default)+'",')
  print('"visible":"'+str(visible)+'",')
  print('"value":"'+node['value']+'",')
  print('"parent":"'+node['parent']+'",')
  print('"id":"'+str(node['id'])+'"')
  print("}")
print("}")

