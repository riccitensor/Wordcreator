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
    auid = str(sys.argv[2]) #author_id
else:
    auid = ""



and_author = ""
if (author_id!=""):
    and_author = """ and w.author_id='"""+author_id+""" '


gdb = GraphDatabase("http://localhost:7474/db/data/")

#q = """MATCH (w:Word) WHERE w.value=~'"""+filtr+""".*' """+and_author+""" return {id: id(w), value: w.value, time_create:w.time_create, author_name:w.author_name} """


q = """MATCH (w:Word) WHERE w.value=~'"""+filtr+""".*'                    return {id: id(w), value: w.value, time_create:w.time_create, author_name:w.author_name} """
//"""+and_author+"""
print(q)


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

  if node['author_name'] is None:
    author_name = "unknow"
  else:
    author_name = node['author_name']




  if (licznik>1): 
     print(',')
  print('"'+str(licznik)+'": {')
  print('"time_create":"'+str(time_create)+'",')
  print('"author_name":"'+str(author_name)+'",')
  print('"value":"'+node['value']+'",')
  print('"id":"'+str(node['id'])+'"')
  print("}")
print("}")

